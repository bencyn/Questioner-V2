import json ,unittest,instance,datetime
from .base_tests import BaseTest
from app import create_app

app = create_app("testing")

class TestMeetup(BaseTest):
    pass
if __name__ == "__main__":
    unittest.main()
   

    