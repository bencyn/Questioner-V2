import json ,unittest,instance,datetime
from .base_tests import BaseTest
from app import create_app

app = create_app("testing")

class TestUser(BaseTest):
    def setUp(self):
        """ defining test data"""
        app.config.from_object(instance.config.TestingConfig)
        self.client = app.test_client()

        self.users =[
            {
                "firstname" :"benson",
                "lastname": "kamaa",
                "othername" :"wamolito",
                "email" :"bensonnjung39@gmail.com",
                "password":"ben74285",
                "phoneNUmber":"0790561841",
                "username" :"njeru",
                "isAdmin" :"0",
            },
            {
                "firstname" :"benson",
                "lastname": "kamaa",
                "othername" :"wamolito",
                "email" :"bensonnjung39@gmail.com",
                "password":"ben74285",
                "phoneNUmber":"0790561841",
                "username" :"njeru",
                "isAdmin" :"0",
            }
        ]
        self.post_url = 'api/v1/users/'
        self.get_url = 'api/v1/users/all'

    def test_if_user_can_create_account(self):
        with self.client:
            ''' test user can create an account successfully'''
            response= self.client.post(self.post_url, data = json.dumps(self.users[0]), content_type="application/json")
            self.assertEqual(response.status_code, 201)

    def test_empty_post_data(self):
        self.user2=[]
        response= self.client.post(self.post_url, data = json.dumps(self.user2), content_type="application/json")
        self.assertEqual(response.status_code,409)

    def test_required_username_email_and_password(self):
        self.user3={
                "firstname" :"benson",
                "lastname": "kamaa",
                "othername" :"wamolito",
                "email" :"",
                "password":"",
                "phoneNUmber":"0790561841",
                "username" :"",
                "isAdmin" :"0"
            }
        response= self.client.post(self.post_url, data = json.dumps(self.user3), content_type="application/json")
        self.assertEqual(response.status_code,400)

    def test_get_all_users(self):
        response = self.client.get(self.get_url,content_type = "application/json")
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_id(self):
        self.get_by_id_url = 'api/v1/users/2'
        self.client.post(self.post_url, data = json.dumps(self.users[0]), content_type="application/json")
        self.client.post('api/v1/meetups/', data = json.dumps(self.users[1]), content_type="application/json")

        response = self.client.get(self.get_by_id_url, content_type="application/json")
        self.assertEqual(response.status_code,200)