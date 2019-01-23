import json ,unittest,instance,datetime
from .base_tests import BaseTest
from app import create_app

app = create_app("testing")

class TestMeetup(BaseTest):
    def setUp(self):
        BaseTest.setUp(self)
        self.get_meetup_url='api/v2/meetups/upcoming'
        self.post_meetup_url=None
        
    def test_user_can_create_meeetup_record(self):
            ''' test user can create a meetup record'''
            # self.client.post(self.register_url, data = json.dumps(self.users[0]), content_type="application/json")
            # login_response = self.client.post(self.login_url, data = json.dumps(self.loging_data), content_type="application/json") 
            # login_result = json.loads(login_response.data.decode('utf-8'))
            # print(login_result)
            # id = login_result["data"][0]["user"][0]["id"]
            # self.post_meetup_url='api/v2/auth/{}/meetups'.format(id)
            self.post_meetup_url='api/v2/auth/1/meetups'
            
            response= self.client.post(self.post_meetup_url,data = json.dumps(self.meetups[0]), 
                                                        content_type="application/json",headers=self._get_header())
            result = json.loads(response.data.decode('UTF-8'))
            print(result)
            self.assertEqual(response.status_code, 201)
   
    def test_user_can_get_meetup_records(self):
        ''' test user can get all meetup records '''
        self.post_meetup_url='api/v2/auth/1/meetups'
            
        self.client.post(self.post_meetup_url,data = json.dumps(self.meetups[0]), 
                                                        content_type="application/json",headers=self._get_header())
                                                        
        response = self.client.get(self.get_meetup_url,content_type = "application/json")
        self.assertEqual(response.status_code, 200)

    # def test_user_can_get_specific_meetup_record(self):
    #     ''' test whether user can get a specific record using it's meetup id '''

    #     self.client.post(self.post_url, data = json.dumps(self.meetups[0]), content_type="application/json",headers=self._get_header())
    #     self.client.post('api/v1/meetups/', data = json.dumps(self.meetups[1]), content_type="application/json",headers=self._get_header())

    #     response = self.client.get(self.get_url, content_type="application/json",headers=self._get_header())
    #     result = json.loads(response.data.decode('UTF-8'))
    #     self.assertEqual(response.status_code,200)
    #     self.assertEqual(result["topic"],"Ethical Hacking Hackathon")

    # def test_rsvp_meetup(self):
    #     ''' tests whether user can respond to a meeting invitation '''

    #     rsvp_url ='api/v1/meetups/1/rsvps'

    #     # post two meetup records
    #     self.client.post('api/v1/meetups/', data = json.dumps(self.meetups[0]), content_type="application/json",headers=self._get_header())
    #     self.client.post('api/v1/meetups/', data = json.dumps(self.meetups[1]), content_type="application/json",headers=self._get_header())
    #     self.client.post('api/v1/meetups/', data = json.dumps(self.meetups[1]), content_type="application/json",headers=self._get_header())
        
    #     response = self.client.post(rsvp_url,data=json.dumps(self.rsvp) ,content_type="application/json",headers=self._get_header())
    #     result = json.loads(response.data.decode('UTF-8'))
    #     self.assertEqual(response.status_code,201)
    #     self.assertEqual(result["data"]['status'],'yes')