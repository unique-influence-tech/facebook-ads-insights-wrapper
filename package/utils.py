"""
"""
import random

from datetime import date, timedelta

def generate_dummy_data(records=10):
    """Generate a simple dummy data set."""
    _list = []
    for _ in range(records):
        length = random.randrange(1, 5)
        record = _generate_dummy_record()
        for __ in range(length):
            click = random.randrange(1,50)
            view = random.randrange(1,50)
            random_action = '<[Fake Action {action}]>'.format(
                action=random.randrange(1, 1000))
            insert = {'action_type': random_action,
                '28d_click': click, 
                '1d_view': view}
            record['actions'].append(insert)
        _list.append(record)
    return _list

def _generate_dummy_record():
    """Generate dummy data for testing."""
    ad_id = random.randrange(100000,999999)
    impressions = random.randrange(100000,999999)
    spend = random.randrange(100,1000)
    inline_link_clicks = random.randrange(25,300)
    date_stop = (date.today()-timedelta(days=random.randrange(1,60))).strftime('%Y-%m-%d')
    date_start = (date.today()-timedelta(days=random.randrange(1,60))).strftime('%Y-%m-%d')
    
    record = {
        'date stop':str(date_stop),
        'date start':str(date_start),
        'campaign_name':'l33t campaign',
        'adset_name':'sUper l33t adset',
        'ad_id': str(ad_id),
        'impressions':str(impressions),
        'spend':str(spend),
        'inline_link_clicks':str(inline_link_clicks),
        'actions':[]}

    return record 


    

