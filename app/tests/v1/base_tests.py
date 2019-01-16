import unittest
from app import create_app

class BaseTest(unittest.TestCase):
    '''test configurations'''

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()

