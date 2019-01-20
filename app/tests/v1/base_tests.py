import json ,unittest,instance,datetime
from app import create_app

class BaseTest(unittest.TestCase):
    '''test configurations'''

    # def setUp(self):
    #     self.app = create_app("testing")
    #     self.client = self.app.test_client()
    #     self.app_context = self.app.app_context()

    def setUp(self):
        """ defining test data"""
     
        self.app = create_app("testing")
        self.app.config.from_object(instance.config.TestingConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
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

        # Get user token
        self._post_register_request(self.users[0])
        self.loging_data = {"username":"bencyn","password":"ben742285"}
        
        # meetup data fields
        self.meetups = [
            {
                "location":"nairobi",
                "topic":"Hackathon For The Brave",
                "happeningOn":"2019-20-23",
                "tags":"UI,UX",
                "images":"https://bencyn.github.io/Questioner/UI/images/456471610.jpeg,https://bencyn.github.io/Questioner/UI/images/475058220.jpeg"
            
            },
            {
                "location":"nyahururu",
                "topic":"Ethical Hacking Hackathon",
                "happeningOn":"Monday 12 2018",
                "tags": ["Pentests", "Bruteforce"],
                "images":"https://bencyn.github.io/Questioner/UI/images/456470.jpeg,https://bencyn.github.io/Questioner/UI/images/475058220.jpeg"
            
            }]
        self.rsvp={"status":"yes"}
        self.get_url = 'api/v1/meetups/2'
        self.post_url ='api/v1/meetups/'
        self.meetup = {
            "topic": "Ethical Hacking Hackathon",
            "location": "Nairobi",
            "images": ["image3.png", "image4.png"],
            "happeningOn": "Monday 12 2018",
            "tags":"Pentests,Bruteforce"
        }
        self.meetups = [
            {
                "location":"nairobi",
                "topic":"Hackathon For The Brave",
                "happeningOn":"2019-20-23",
                "tags":"UI,UX",
                "images":"https://bencyn.github.io/Questioner/UI/images/456471610.jpeg,https://bencyn.github.io/Questioner/UI/images/475058220.jpeg"
            
            },
            {
                "location":"nyahururu",
                "topic":"Ethical Hacking Hackathon",
                "happeningOn":"Monday 12 2018",
                "tags": "pentests,codebase",
                "images":"https://bencyn.github.io/Questioner/UI/images/456470.jpeg,https://bencyn.github.io/Questioner/UI/images/475058220.jpeg"
            
            }]
        self.rsvp={"status":"yes"}
        self.get_url = 'api/v1/meetups/2'
        self.post_url ='api/v1/meetups/'
        # question data fields
        self.question= { "title": "gnome series",
                               "body":"Attending the gnome series shoot"}
        self.question_er= {"title":""}

        self.question_upvoted = {"body": "Attending the gnome series shoot",
                                 "meetup": 1,
                                 "user": 1,
                                 "question_id": 1,
                                 "title": "gnome series",
                                 "votes": 1}

        self.question_downvoted = {"body": "Attending the gnome series shoot",
                                 "meetup": 1,
                                 "user": 1,
                                 "question_id": 1,
                                 "title": "gnome series",
                                 "votes": 0}
        self.response_question=[{"body": "I would like to know the kind of food being served at the meetup",
                                           "meetup": 1,
                                           "title": "what are we to eat?"}]

        self.upvote_response ={
                                "body": "Attending the gnome series shoot",
                                "meetup": 1,
                                "title": "gnome series",
                                "user_id": 1,
                                "votes": 1
                            }
        self.downvote_response ={
                                "body": "Attending the gnome series shoot",
                                "meetup": 1,
                                "title": "gnome series",
                                "user_id": 1,
                                "votes": 0
                            }
  
    
    def _get_header(self):
        """return user header with token"""
        self.client.post(self.register_url, data = json.dumps(self.users[0]), content_type="application/json")
        self.client.post(self.register_url, data = json.dumps(self.users[1]), content_type="application/json")
       
        login_response =self._post_login_request(self.loging_data)
        login_result =json.loads(login_response.data.decode('utf-8'))
        if login_response:
            token = login_result["data"]["token"]

        self.headers = {
            'Authorization': 'Bearer {}'.format(token),
            'Content-Type': 'application/json'
        }

        return self.headers

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
       
        