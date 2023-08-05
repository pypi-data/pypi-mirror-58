"""
Manager class for getting datadog data for isitfit

Pre-requisites
    pip3 install datadog asciiplotlib pandas
    apt-get install gnuplot

set env vars
    export DATADOG_API_KEY=...
    export DATADOG_APP_KEY=...
    
Run tests
    pip3 install pytest
    pytest datadogManager.py
"""

import json
import time
import pandas as pd
import os

from isitfit.utils import logger


# Configure the module according to your needs
from datadog import initialize

# Use Datadog REST API client
from datadog import api

SECONDS_IN_ONE_DAY = 60*60*24

class DdgNoData(ValueError):
  pass

class HostNotFoundInDdg(DdgNoData):
  pass

class DataNotFoundForHostInDdg(DdgNoData):
  pass

def raise_hostNotFound():
  raise HostNotFoundInDdg

def raise_dataNotFound():
  raise DataNotFoundForHostInDdg

class DataQueryError(ValueError):
  pass

class DatadogAssistant:
    def __init__(self, start, end, host_id):
        self.end = end
        self.start = start
        self.host_id = host_id

    def _get_metrics_core(self, query, col_i):
        m = api.Metric.query(start=self.start, end=self.end, query=query, host=self.host_id)
        if m['status']=='error':
          raise DatadogQueryError(m['error'])

        if len(m['series'])==0:
            raise DataNotFoundForHostInDdg("No %s found for %s"%(col_i, self.host_id))

        df = pd.DataFrame(m['series'][0]['pointlist'], columns=['ts_int', col_i])
        df['ts_dt'] = pd.to_datetime(df.ts_int, origin='unix', unit='ms')
        del df['ts_int']
        return df
        
    def _get_meta(self):
        h_all = api.Hosts.search(host=self.host_id)
        if len(h_all['host_list'])==0:
            raise HostNotFoundInDdg("Did not find host %s in datadog"%self.host_id)

        h_i = h_all['host_list'][0]
        gohai = json.loads(h_i['meta']['gohai'])
        memory_total = int(gohai['memory']['total'].replace('kB',''))*1024
        out = {'cpuCores': h_i['meta']['cpuCores'], 'memory_total': memory_total}
        return out
        
    def get_metrics_cpu_max(self):
        # query language
        # https://docs.datadoghq.com/graphing/functions/
        # Use minimum so that cpu_used will be the maximum
        query = 'system.cpu.idle{host:%s}.rollup(min,%i)'%(self.host_id, SECONDS_IN_ONE_DAY)
        col_i = 'cpu_idle_min'
        df = self._get_metrics_core(query, col_i)
        # calculate cpu used as 100 - cpu_idle
        df['cpu_used_max'] = 100 - df.cpu_idle_min
        df['cpu_used_max'] = df['cpu_used_max'].astype(int)
        return df

    def get_metrics_cpu_min(self):
        # query language
        # https://docs.datadoghq.com/graphing/functions/
        # Use minimum so that cpu_used will be the maximum
        query = 'system.cpu.idle{host:%s}.rollup(max,%i)'%(self.host_id, SECONDS_IN_ONE_DAY)
        col_i = 'cpu_idle_max'
        df = self._get_metrics_core(query, col_i)
        # calculate cpu used as 100 - cpu_idle
        df['cpu_used_min'] = 100 - df.cpu_idle_max
        df['cpu_used_min'] = df['cpu_used_min'].astype(int)
        return df
        
    def get_metrics_cpu_avg(self):
        # repeat for average
        query = 'system.cpu.idle{host:%s}.rollup(avg,%i)'%(self.host_id, SECONDS_IN_ONE_DAY)
        col_i = 'cpu_idle_avg'
        df = self._get_metrics_core(query, col_i)
        df['cpu_used_avg'] = 100 - df.cpu_idle_avg
        df['cpu_used_avg'] = df['cpu_used_avg'].astype(int)
        return df

    def get_metrics_ram_max(self):
        # query language, check note above in get_metrics_cpu
        query = 'system.mem.free{host:%s}.rollup(min,%i)'%(self.host_id, SECONDS_IN_ONE_DAY)
        col_i = 'ram_free_min'
        df =  self._get_metrics_core(query, col_i)
        memory_total = self._get_meta()['memory_total']
        df['ram_free_min'] = df.ram_free_min / memory_total * 100
        df['ram_free_min'] = df['ram_free_min'].astype(int)
        df['ram_used_max'] = 100 - df['ram_free_min']
        return df

    def get_metrics_ram_min(self):
        # query language, check note above in get_metrics_cpu
        query = 'system.mem.free{host:%s}.rollup(max,%i)'%(self.host_id, SECONDS_IN_ONE_DAY)
        col_i = 'ram_free_max'
        df =  self._get_metrics_core(query, col_i)
        memory_total = self._get_meta()['memory_total']
        df['ram_free_max'] = df.ram_free_max / memory_total * 100
        df['ram_free_max'] = df['ram_free_max'].astype(int)
        df['ram_used_min'] = 100 - df['ram_free_max']
        return df

    def get_metrics_ram_avg(self):
        # query language, check note above in get_metrics_cpu
        query = 'system.mem.free{host:%s}.rollup(avg,%i)'%(self.host_id, SECONDS_IN_ONE_DAY)
        col_i = 'ram_free_avg'
        df =  self._get_metrics_core(query, col_i)
        memory_total = self._get_meta()['memory_total']
        df['ram_free_avg'] = df.ram_free_avg / memory_total * 100
        df['ram_free_avg'] = df['ram_free_avg'].astype(int)
        df['ram_used_avg'] = 100 - df['ram_free_avg']
        return df

    def get_metrics_count(self):
        # query language, check note above in get_metrics_cpu
        query = 'count_not_null(system.mem.free{host:%s})'%(self.host_id)
        col_i = 'nhours'
        df1 =  self._get_metrics_core(query, col_i)
        # yields data per hour, so process in pandas to daily
        df2 = df1.set_index('ts_dt').resample('1D').nhours.sum().reset_index()
        return df2


class DatadogManager:
    def __init__(self):
        initialize()
        self.set_ndays(90) # default is 90 days
        self.print_configured = True

    def set_ndays(self, ndays):
        self.ndays = ndays
        self.end = int(time.time())
        
        # datadog will automatically set the resolution based on the start-end range
        # if the ".rollup" is not used in the query
        # number of seconds in 1 hour, if no ".rollup" specified in query, this yields 20-second frequency from datadog
        # n_secs = 60*60
        # number of seconds in 90 days, if no ".rollup" specified in query, yields bi-daily from datadog
        n_secs = SECONDS_IN_ONE_DAY*self.ndays
        self.start = self.end - n_secs


    def is_configured(self):
      # check not None and not empty string
      if os.getenv('DATADOG_API_KEY', None):
        if os.getenv('DATADOG_APP_KEY', None):
          if self.print_configured:
            logger.info("Datadog env vars available")
            self.print_configured = False
          return True
          
      if self.print_configured:
        logger.info("Datadog env vars missing. Set DATADOG_API_KEY and DATADOG_APP_KEY to get memory data from Datadog.")
        self.print_configured = False

      return False


    def get_metrics_all(self, host_id):
        # FIXME: we already have cpu from cloudwatch, so maybe just focus on ram from datadog
        logger.debug("Fetching datadog data for %s"%host_id)
        ddgL2 = DatadogAssistant(self.start, self.end, host_id)
        df_cpu_max = ddgL2.get_metrics_cpu_max()
        df_cpu_min = ddgL2.get_metrics_cpu_min()
        df_cpu_avg = ddgL2.get_metrics_cpu_avg()
        df_ram_max = ddgL2.get_metrics_ram_max()
        df_ram_min = ddgL2.get_metrics_ram_min()
        df_ram_avg = ddgL2.get_metrics_ram_avg()
        df_count   = ddgL2.get_metrics_count()
        df_all = (
            df_cpu_max
            .merge(df_cpu_min, how='outer', on=['ts_dt'])
            .merge(df_cpu_avg, how='outer', on=['ts_dt'])
            .merge(df_ram_max, how='outer', on=['ts_dt'])
            .merge(df_ram_min, how='outer', on=['ts_dt'])
            .merge(df_ram_avg, how='outer', on=['ts_dt'])
            .merge(df_count,   how='outer', on=['ts_dt'])
        )
        df_all = df_all[['ts_dt', 'cpu_used_max', 'cpu_used_min', 'cpu_used_avg', 'ram_used_max', 'ram_used_min', 'ram_used_avg', 'nhours']]

        # convert from datetime to date to be able to merge with cloudtrail
        df_all['ts_dt'] = df_all.ts_dt.dt.date

        # rename like cloudwatch
        df_all.rename(columns={'ts_dt': 'Timestamp'}, inplace=True)

        return df_all


from .cacheManager import MetricCacheMixin


class DatadogCached(MetricCacheMixin, DatadogManager):
    def get_key(self, host_id):
        cache_key = "datadog:cpu+ram:%s:%i"%(host_id, self.ndays)
        return cache_key

    def get_metrics_derived(self, rc_describe_entry, rc_id, rc_created):
      return super().get_metrics_all(rc_id)


#class DatadogListener(DatadogCached):
#    """
#    A listener for the Event Bus defined in mainManager.py
#    """
#    def per_ec2(self, context_ec2):
#        raise Exception("Deprecated")
#
#        if not self.is_configured():
#          context_ec2['ddg_df'] = None
#          return context_ec2
#
#        # parse out keys
#        host_id = context_ec2['ec2_obj'].instance_id
#
#        # get data
#        ddg_df = self.get_metrics_all(host_id)
#
#        if ddg_df is None:
#          context_ec2['ddg_df'] = None
#          return context_ec2
#
#        # add to context
#        context_ec2['ec2_df'] = ec2_df # update context
#        context_ec2['ddg_df'] = ddg_df
#
#        # return
#        return context_ec2
#
