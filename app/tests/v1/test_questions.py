import json ,unittest,instance,datetime
from .base_tests import BaseTest
from app.api.v1.views import questions_view
from app import create_app

app = create_app("testing")

class QuestionTest(BaseTest):
    
    def test_user_upvote_question(self):
        self.client.post("api/v1/meetups/", data = json.dumps(self.meetups[0]), content_type = "application/json", headers=self._get_header())
        self.client.post("api/v1/meetups/1/questions", data = json.dumps(self.question), content_type = "application/json", headers=self._get_header())
        response = self.client.patch("api/v1/questions/1/upvote", 
                    content_type = "application/json",
                    headers=self._get_header())
        result = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['data']["body"],self.upvote_response["body"] )

    def test_question_upvote_if_question_not_found(self):

        self.client.post("api/v1/meetups/", data = json.dumps(self.meetups[0]), content_type = "application/json",headers=self._get_header())
        self.client.post("api/v1/meetups/1/questions", data = json.dumps(self.question), content_type = "application/json",headers=self._get_header())
        
        response = self.client.patch("api/v1/questions/30/upvote", content_type = "application/json",headers=self._get_header())
        result =json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(result["error"],"Question not found")

    def test_user_downvote_question(self):
    
        self.client.post("api/v1/meetups/", data = json.dumps(self.meetups[0]), content_type = "application/json",headers=self._get_header())
        self.client.post("api/v1/meetups/1/questions", data = json.dumps(self.question), content_type = "application/json",headers=self._get_header())
        
        response = self.client.patch("api/v1/questions/1/downvote", content_type = "application/json",headers=self._get_header())
        result =json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['data']["body"],self.downvote_response["body"])

    def test_question_downvote_if_question_not_found(self):

        self.client.post("api/v1/meetups/", data = json.dumps(self.meetups[0]), content_type = "application/json",headers=self._get_header())
        self.client.post("api/v1/meetups/1/questions", data = json.dumps(self.question), content_type = "application/json",headers=self._get_header())
        
        response = self.client.patch("api/v1/questions/4/downvote", content_type = "application/json",headers=self._get_header())
        result =json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(result["error"],"Question not found")

    def user_can_post_question(self):
        
        self.client.post("api/v1/meetups/", data = json.dumps(self.meetups[0]), content_type = "application/json", headers=self._get_header())
        response = self.client.post("api/v1/meetups/1/questions", data = json.dumps(self.question), content_type = "application/json", headers=self._get_header())
        result = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['status'], 201)
        self.assertEqual(result['data'],self.response_question)
