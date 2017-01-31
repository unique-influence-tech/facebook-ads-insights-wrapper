from package.parameters import ATTRIBUTION, STATUS, ACTIONS

# COMMON CONVERSION ATTRIBUTION
STRICT = [ATTRIBUTION.one_day_click, ATTRIBUTION.one_day_view]
NORMAL = [ATTRIBUTION.twenty_eight_day_click, ATTRIBUTION.one_day_view]
LOOSE = [ATTRIBUTION.twenty_eight_day_click, ATTRIBUTION.twenty_eight_day_view]
ALL_ATTR= [getattr(ATTRIBUTION, _) for _ in dir(ATTRIBUTION) if not '__' in _ and _ != 'default']

# COMMON STATUSES
ALL_STATUS = [getattr(STATUS, _) for _ in dir(STATUS) if not '__' in _]

# COMMON ACTION SETS
NORMAL_ACTION = [ACTIONS.actions, ACTIONS.action_values]
ALL_ACTIONS = [getattr(ACTIONS, _) for _ in dir(ACTIONS) if not '__' in _]

# TEST VARS
TEST_QUERY = { 
    'time_increment': 1, 
    'filtering': [
        {'operator':"GREATER_THAN",
        'field':"ad.impressions",
        'value':0},
        {'operator': 'IN', 
        'field': 'ad.effective_status', 
        'value': ALL_STATUS},
        {'operator': 'IN', 
        'field': 'action_type', 
        'value': [
            'offsite_conversion.fb_pixel_purchase', 
            'offsite_conversion.fb_pixel_purchase']}], 
    'level': 'ad', 
    'fields': [
        'ad_id',
        'campaign_name',
        'adset_name',
        'impressions',
        'inline_link_clicks',
        'spend'] + NORMAL_ACTION, 
    'date_preset': 'last_30_days',
    'action_attribution_windows': NORMAL}
    
TEST_QUERY_2 = { 
    'time_increment': 1, 
    'filtering': [
        {'operator':"GREATER_THAN",
        'field':"campaign.impressions",
        'value':0},
        {'operator': 'IN', 
        'field': 'ad.effective_status', 
        'value': ALL_STATUS}], 
    'level': 'campaign', 
    'fields': [
        'campaign_id',
        'campaign_name',
        'impressions',
        'inline_link_clicks',
        'spend'] + [ACTIONS.actions], 
    'time_range':{'since':'2016-02-01', 'until':'2017-01-22'},
    'action_attribution_windows': LOOSE}

TEST_QUERY_3 = {
 'action_attribution_windows': ['28d_click', '28d_view'],
 'fields': [
    'ad_id',
    'campaign_name',
    'adset_name',
    'impressions',
    'inline_link_clicks',
    'spend',
    'actions'
 ],
 'time_range': {'since':'2016-07-01', 'until':'2016-12-19'},
 'time_increment': 1,
 'filtering': [
    {'field': 'ad.effective_status',
     'value': ALL_STATUS,
     'operator': 'IN'},
     {'operator':"GREATER_THAN",
      'field':"ad.impressions",
      'value':0},
    {'field':'action_type',
    'operator':'IN', 
    'value':[
        'offsite_conversion.custom.537558553106725',
        'offsite_conversion.custom.315325215468764',
        'offsite_conversion.custom.1773776782837176',
        'offsite_conversion.custom.1189968604415585',
        'offsite_conversion.custom.910760072356997',
        'offsite_conversion.custom.1200902003311910']
    }],
 'breakdowns': ['impression_device'],
 'action_breakdowns': [
    'action_device', 
    'action_type'],
 'level': 'ad',
 'action_attribution_windows': NORMAL}
