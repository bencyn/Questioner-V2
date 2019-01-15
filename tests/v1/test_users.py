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
                "password":"ben742285",
                "phoneNUmber":"0790561841",
                "username" :"bencyn",
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
        self.register_url = 'api/v1/users/'
        self.get_url = 'api/v1/users/all'
        self.login_url = 'api/v1/users/login'

    def test_if_user_can_create_account(self):
        with self.client:
            ''' test user can create an account successfully'''
            response= self.client.post(self.register_url, data = json.dumps(self.users[0]), content_type="application/json")
            self.assertEqual(response.status_code, 201)

    def test_empty_register_post_data(self):
        self.user2=[]
        response= self.client.post(self.register_url, data = json.dumps(self.user2), content_type="application/json")
        self.assertEqual(response.status_code,409)

    def test_required_username_email_and_password_on_register(self):
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
        response = self._post_register_request(self.user3)
        self.assertEqual(response.status_code,400)

    def test_missing_register_data(self):
        response = self._post_register_request()
        self.assertEqual(response.status_code,400)
    
    def test_get_all_users(self):
        response = self.client.get(self.get_url,content_type = "application/json")
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_id(self):
        self.get_by_id_url = 'api/v1/users/2'
        self.client.post(self.register_url, data = json.dumps(self.users[0]), content_type="application/json")
        self.client.post(self.register_url, data = json.dumps(self.users[1]), content_type="application/json")

        response = self.client.get(self.get_by_id_url, content_type="application/json")
        self.assertEqual(response.status_code,200)
    
    def test_if_user_can_login(self):
        """ tests if user can login successfully with correct credentials """

        self.loging_data = {"username":"bencyn","password":"ben742285"}
        self._post_register_request(self.users[0])
        response = self._post_login_request(self.loging_data)
        self.assertEqual(response.status_code,201)
        # test if data output matches our input
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["data"]["username"],self.loging_data["username"])
        self.assertEqual(result["data"]["password"],self.loging_data["password"])
      
    
    def test_login_username_empty(self):
        """tests if user can login with an empty username string provided"""

        self.username_empty={"username":"","password":"ben742285"}
        self._post_register_request(self.users[0])
        response = self._post_login_request(self.username_empty)

        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code,400)
        self.assertEqual(result["error"],"username cannot be empty")

    def test_login_password_empty(self):
        """tests if user can login with an empty password string provided"""

        self.password_empty={"username":"bencyn","password":""}
        self._post_register_request(self.users[0])
        response = self._post_login_request(self.password_empty)
        self.assertEqual(response.status_code,400)
        result =json.loads(response.data)
        self.assertEqual(result["error"],"password cannot be empty")
       

    def test_missing_login_data(self):
        """ tests if user can login without providing any data """

        response = self._post_login_request()
        self.assertEqual(response.status_code,400)

        result= json.loads(response.data)
        self.assertEqual(result["error"],"Bad request: attach missing fields")
    
    def _post_login_request(self,input=""):
        """ sends a post login request with the input passed as data """
        if input:
            self.data = json.dumps(input)
            response = self.client.post(self.login_url, data = self.data, content_type="application/json")
        else:
            response = self.client.post(self.login_url,content_type="application/json")

        return response
   
    def _post_register_request(self,input=""):
        """ send a post regiter request with the input passed as data"""
        if input is True:
            response = self.client.post(self.register_url, data = self.data, content_type="application/json")
        else:
            response = self.client.post(self.register_url,content_type="application/json")

        return response
       
        
    