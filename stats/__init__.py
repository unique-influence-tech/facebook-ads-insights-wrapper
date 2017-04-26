# -*- coding: utf-8 -*-
'''
Make large requets to the /insights endpoint. 

Basic Usage:
    >> import stats
    >> query = stats.insights.Query('1234356789', prepared_stats_request)
    >> query.schedule_job()
    >> query.retrieve_job()
'''
import stats.insights
