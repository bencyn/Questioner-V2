import json ,unittest,instance,datetime
from .base_tests import BaseTest
from app import create_app

app = create_app("testing")

class TestUser(BaseTest):

    # def test_if_user_can_create_account(self):
    #     ''' test user can create an account successfully'''
    #     response= self.client.post(self.register_url, data = json.dumps(self.users[0]), content_type="application/json")
    #     self.assertEqual(response.status_code, 201)

    def test_empty_register_post_data(self):
        """ test if user can register with empty data"""
        self.user2=[]
        response= self.client.post(self.register_url, data = json.dumps(self.user2), content_type="application/json")
        self.assertEqual(response.status_code,409)

    def test_required_username_email_and_password_on_register(self):
        """ tests if  username and password is required on register """
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
     
        response = self.client.get(self.get_url,
                                    content_type = "application/json",
                                    headers=self._get_header()
                                )
        self.assertEqual(response.status_code, 200)
        

    def test_get_user_by_id(self):
        self.get_by_id_url = 'api/v2/auth/1'
        
        response = self.client.get(self.get_by_id_url, 
                                    content_type="application/json",
                                    headers=self._get_header())

        self.assertEqual(response.status_code,200)
        result = json.loads(response.data.decode('utf-8'))
        # self.assertEqual(result["username"],self.users[1]["username"])

  
    def test_if_user_can_login(self):
        """ tests if user can login successfully with correct credentials """
       
        self._post_register_request(self.users[0])
        response = self._post_login_request(self.loging_data)
        self.assertEqual(response.status_code,201)
        # test if data output matches our input
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["message"],'user logged in successfully')
        # self.assertEqual(result["data"]["password"],self.loging_data["password"])
      
    
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
    

    