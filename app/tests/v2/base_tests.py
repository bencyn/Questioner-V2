import unittest
from app import create_app
from ... import create_app
# from ...api.v2.database.database_connection import (create_database_tables,
#                                                     drop_all_tables, 
#                                                     all_test_data)
from app.database.connect import (test_db_init,drop_tables)

class BaseTest(unittest.TestCase):
    '''main test configurations '''

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            self.test_db = test_db_init()
        """ defining test data"""

        # users test data
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
        self.register_url = 'api/v2/users/'
        self.get_url = 'api/v2/users/all'
        self.login_url = 'api/v2/users/login'
        
        # meetup test data
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

        # question test data
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
        # meetup data
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
        self.get_url = 'api/v2/meetups/2'
        self.post_url ='api/v2/meetups/'