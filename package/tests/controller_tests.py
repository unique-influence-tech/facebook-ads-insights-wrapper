import unittest
import mock 

from package.insights import Controller
from package.utils import generate_dummy_data
from package.tests.dummy_values import TEST_QUERY

class ControllerTests(unittest.TestCase):

    def setUp(self):
        self.large_test_records = generate_dummy_data(5)
        self.small_test_records = generate_dummy_data(1)
        self.test_query = TEST_QUERY

    def test_get_unique_actions(self):
        test_set = set()
        empty_set = set()
        obj = Controller
        mok = mock.Mock(spec=obj)
        mok.side_effect = obj._Controller__get_unique_actions
        resp = mok(mok, self.large_test_records)
        empty_resp = mok(mok, {})
        for record in self.large_test_records:
            fake_actions = record.get('actions')
            for action in fake_actions:
                test_set.add(action['action_type'])
        self.assertIsInstance(resp, set)
        self.assertSetEqual(resp, test_set)
        self.assertSetEqual(empty_resp, empty_set)

    def test_construct_base_record(self):
        obj = Controller
        mok = mock.Mock(spec=obj)
        mok._query = TEST_QUERY
        mok._raw = self.small_test_records
        actions_return_value = obj._Controller__get_unique_actions(mok, mok._raw)
        mok._Controller__get_unique_actions.return_value = actions_return_value
        mok.side_effect = obj._Controller__construct_base_record
        test_keys = mok(mok).keys()
        check_1 = []
        for field in test_keys:
            if 'Fake' not in field and field in mok._query['fields']:
                check_1.append(True)
        check_2 = []
        for action in actions_return_value:
            if action in test_keys:
                check_2.append(True)
        self.assertTrue(all(check_1))
        self.assertTrue(all(check_2))

    def test_handle_actions(self):
        obj = Controller
        mok = mock.Mock(spec=obj)
        records = self.large_test_records
        for record in records:
            mok.side_effect = obj._Controller__handle_actions(mok, record['actions'])       
            action_num = 0
            for item in record['actions']:
                action_num += 1
            resp = {} 
            for item in mok.side_effect:
                resp.update(item)
            # See package.utils 
            self.assertEqual(len(resp), action_num*2) 

    def test_poll(self):
        obj = Controller
        mok = mock.Mock(spec=obj)
        mok._Controller__poll.return_value = ('<[Job Id 12345678 100% complete]>')
        resp = mok._Controller__poll(mok)
        self.assertIsInstance(resp, str)

    def test_get_job_id(self):
        obj = Controller
        mok = mock.Mock(spec=obj)
        mok._job_id = '12345678'
        mok.job_id.return_value = mok._job_id
        resp = mok.job_id()
        self.assertIsInstance(resp, str)

    def test_get_data(self):
        obj = Controller
        mok = mock.Mock(spec=obj)
        mok._response = self.large_test_records
        mok.data.return_value = mok._response
        resp = mok.data()
        self.assertIsInstance(resp, list)

    def test_retrieve_job(self):
        #TODO: Mock these calls completely.
        pass
        
    def test_schedule_job(self):
        # TODO: Mock these calls compeletely. 
        pass

    def test_call(self):
        # TODO: Mock these calls compeletely.
        pass





