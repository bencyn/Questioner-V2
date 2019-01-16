import json ,unittest,instance,datetime
from .base_tests import BaseTest
from app.api.v1.views import questions_view
from app import create_app

app = create_app("testing")

class QuestionTest(BaseTest):
    def setUp(self):
        app.config.from_object(instance.config.TestingConfig)
        self.client = app.test_client()
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
  
    def test_user_upvote_question(self):
        self.client.post("api/v1/meetups/", data = json.dumps(self.meetups[0]), content_type = "application/json")
        self.client.post("api/v1/meetups/1/questions", data = json.dumps(self.question), content_type = "application/json")
        response = self.client.patch("api/v1/questions/1/upvote", content_type = "application/json")
        result = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['data']["body"],self.upvote_response["body"] )

    def test_question_upvote_if_question_not_found(self):

        self.client.post("api/v1/meetups/", data = json.dumps(self.meetups[0]), content_type = "application/json")
        self.client.post("api/v1/meetups/1/questions", data = json.dumps(self.question), content_type = "application/json")
        
        response = self.client.patch("api/v1/questions/30/upvote", content_type = "application/json")
        result =json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(result["error"],"Question not found")

    def test_user_downvote_question(self):
    
        self.client.post("api/v1/meetups/", data = json.dumps(self.meetups[0]), content_type = "application/json")
        self.client.post("api/v1/meetups/1/questions", data = json.dumps(self.question), content_type = "application/json")
        
        response = self.client.patch("api/v1/questions/1/downvote", content_type = "application/json")
        result =json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['data']["body"],self.downvote_response["body"])

    def test_question_downvote_if_question_not_found(self):

        self.client.post("api/v1/meetups/", data = json.dumps(self.meetups[0]), content_type = "application/json")
        self.client.post("api/v1/meetups/1/questions", data = json.dumps(self.question), content_type = "application/json")
        
        response = self.client.patch("api/v1/questions/4/downvote", content_type = "application/json")
        result =json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(result["error"],"Question not found")

    def user_can_post_question(self):
        
        self.client.post("api/v1/meetups/", data = json.dumps(self.meetups[0]), content_type = "application/json")
        response = self.client.post("api/v1/meetups/1/questions", data = json.dumps(self.question), content_type = "application/json")
        result = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['status'], 201)
        self.assertEqual(result['data'],self.response_question)
