"""
"""
import json
import pprint

from package.config import (token, app_id, app_secret)
from facebookads import FacebookAdsApi
from facebookads.objects import AdAccount

class Query:
    """ Schedule large jobs, let Facebook process, poll to check and 
    then request job data. 

    Args:
        :acct: str, account id from facebook 
        :prepared: dict, containing specified parameter values

    Refs:
        None
    """
    _API_ = FacebookAdsApi.init(app_id, app_secret, token)
    _GRAPH_URL_ = 'https://graph.facebook.com/v2.9/'

    def __init__(self, acct, prepared=None):
        self._acct = AdAccount('act_{}'.format(acct))
        self._query = prepared 
        self._job_id = None
        self._raw = [] # pre-sorted response
        self._response = []

    # Exposed Methods 
    def schedule_job(self, prepared=None):
        """Schedules job based on passed or internal dict obj."""
        acct = self._acct
        self._query = prepared if prepared else self._query
        params = self._query

        if prepared:             
            job = acct.get_insights(params=params, async=True)
        else:
            job = acct.get_insights(params=params, async=True)

        self._job_id = job.remote_read()['id']

        return True

    def poll(self):
        """Polls FB job id and return percent complete."""
        base = self._GRAPH_URL_+'{0}'

        url = base.format(self._job_id)
        resp = self._API_.call('GET', url)
        resp_json = json.loads(resp.body())

        return ('<[Job Id {job} {perc1}% complete]>').format(
            perc1=resp_json['async_percent_completion'],
            job=resp_json['id'])

    def retrieve_job(self, id=None):
        """Retrieve scheduled job."""
        store = []
        base = self._GRAPH_URL_+'{0}/insights'
        
        if id:  
            url = base.format(id)
        else:
            url = base.format(self._job_id)
        init_resp = self._API_.call('GET', url, params={'limit':1000})
        resp_json = json.loads(init_resp.body())
        
        while resp_json['paging'].get('next'):
            store = store + resp_json['data']
            _next = resp_json['paging']['next']
            resp = self._API_.call('GET', _next, params={'limit':1000})
            resp_json = json.loads(resp.body())
        
        store = store + resp_json['data']
        self._raw = store
        self._response = self.__parse_response(store)

        return self._response

    # Internal Methods
    def __get_actions(self, store):
        """Return unique actions."""
        action_set = set()

        for record in store:
            actions = record.get('actions')
            if actions:
                for action in actions:
                    action_set.add(action['action_type'])

        return action_set
    
    def _make_response_dict(self):
        """Create the default dictionary for records."""
        params = self._query
        actions = self.__get_actions(self._raw)

        fields = [_ for _ in params.get('fields') if 'action' not in _]
        attrs = params.get('action_attribution_windows')

        action_keys = ['%s_%s' % (g, a) for a in attrs for g in actions]
        action_value_keys = ['%s_%s_%s' % (g, a, "value") for a in attrs for g in actions]
        base = ['date'] + fields + action_keys + action_value_keys

        return {item:'' for item in base}

    def __retrieve_job(self):
        """Retrieve scheduled job."""
        store = []
        base = self._GRAPH_URL_+'{0}/insights'
                
        url = base.format(self._job_id)
        init_resp = self._API_.call('GET', url, params={'limit':1000})
        resp_json = json.loads(init_resp.body())
        
        while resp_json['paging'].get('next'):
            store = store + resp_json['data']
            _next = resp_json['paging']['next']
            resp = self._API_.call('GET', _next, params={'limit':1000})
            resp_json = json.loads(resp.body())
        
        store = store + resp_json['data']
        self._raw = store
        self._response = self.__parse_response(store)

        return True

    def __parse_response(self, response):
        """Sort response into list of flat dictionaries."""
        _store = []
        base_record = self._make_response_dict()
        
        for record in response:
            _record = base_record.copy()
            for key, value in record.items():
                if key in base_record.keys():
                    _record.update({key:value})
                elif key == 'date_stop':
                    _record['date'] = record['date_stop']
                elif key == 'actions' or key == 'action_values':
                    flag = False
                    actions = record.get(key)
                    if key == 'action_values':
                        flag = True
                    for _dict in self.__parse_actions(actions, flag):
                        _record.update(_dict)
            _store.append(_record)

        return _store

    def __parse_actions(self, _list, flag=False):
        """Return an actions or action values generator."""
        for action in _list:
            current = {}
            _action = action['action_type']
            for key, value in action.items():
                if key != 'action_type' and key != 'value':
                    _key = '%s_%s' % (_action, key)
                    if flag:
                        _key = '%s_%s_%s' % (_action, key, 'value')
                    current[_key] = value
                else:
                    continue
            yield current

    # Representations 
    def __repr__(self):
        return ('<{name} object at {mem} with stored '
            'query-->[{query}] >').format(
                name=self.__class__.__name__,
                mem=hex(id(self)),
                query=hasattr(self, '_response')
        )

    def __str__(self):
        return '<[FB Query Object]>'

    # Attributes
    @property
    def parameters(self):
        return self._query

    @property
    def data(self):
        return self._response if self_response else (
            "You haven't retrieved a job!")

    @property
    def raw(self):
        '''Return pre-parsed response.'''
        return self._raw












