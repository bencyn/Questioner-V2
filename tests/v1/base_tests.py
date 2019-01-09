'''Global Tests'''

import unittest
from app import create_app
from app.v1.models.meetup_model import meetup 

class BaseTest(unittest.TestCase):
    '''test configurations'''

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()

    
    # def tearDown(self):
    #     '''Removes the dictionaries and the context'''
    #     del user_accounts[:]