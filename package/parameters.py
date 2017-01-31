"""
fb ad read parameters 
"""
# Credit: Twitter Engineering Team
# See @ https://github.com/twitterdev/twitter-python-ads-sdk.
def enum(**enums):
    return type('Enum', (), enums)

LEVEL = enum(
    account='account',
    campaign='campaign',
    adset='adset',
    ad='ad')

DATE_PRESETS = enum(
    today='today',
    yesterday='yesterday',
    last_3_days='last_3_days',
    this_week='this_week',
    last_week='last_week',
    last_7_days='last_7_days',
    last_14_days='last_14_days',
    last_28_days='last_28_days',
    last_30_days='last_30_days',
    last_90_days='last_90_days',
    this_month='this_month',
    last_month='last_month',
    this_quarter='this_quarter',
    last_3_months='last_3_months',
    lifetime='lifetime')

ATTRIBUTION = enum(
    one_day_view='1d_view',
    seven_day_view='7d_view',
    twenty_eight_day_view='28d_view',
    one_day_click='1d_click',
    seven_day_click='7d_click',
    twenty_eight_day_click='28d_click',
    default='default')

STATUS = enum(
    active='ACTIVE',
    disapproved='DISAPPROVED',
    archived='ARCHIVED',
    paused='PAUSED',
    deleted='DELETED')

ACTIONS = enum(
    action_values='action_values',
    actions='actions',
    video_10_sec_watched_actions='video_10_sec_watched_actions',
    video_15_sec_watched_actions='video_15_sec_watched_actions',
    video_30_sec_watched_actions='video_30_sec_watched_actions',
    video_complete_watched_actions='video_complete_watched_actions',
    video_p100_watched_actions='video_p100_watched_actions',
    video_p25_watched_actions='video_p25_watched_actions',
    video_p50_watched_actions='video_p50_watched_actions',
    video_p75_watched_actions='video_p75_watched_actions',
    video_p95_watched_actions='video_p95_watched_actions')

"""
def create_filter_obj(self, **kwargs):
    {'field':'',
    'operator':'',
    'value':[]}
    pass


def create_ads_request(self, campaign, **kwargs):
    base = {
    'fields':[]
    'time_range':{},
    'date_preset':'last 30 days'
    'time_increment': 1,
    'level':,
    'filtering':[]
    'breakdowns':}
    
    {'field':'{entity}.effective_status'.format(entity='campaign'),
    'operator':'IN',
    'value':[]}
    pass
"""





