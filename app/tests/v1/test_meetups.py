import json ,unittest,instance,datetime
from .base_tests import BaseTest
from app import create_app

app = create_app("testing")

class TestMeetup(BaseTest):
  
    def test_user_can_create_meeetup_record(self):
        with self.client:
            ''' test user can create a meetup record'''

            response= self.client.post('api/v1/meetups/',data = json.dumps(self.meetups[0]), 
                                                        content_type="application/json",headers=self._get_header())

            self.assertEqual(response.status_code, 201)
   
    def test_user_can_get_meetup_records(self):
        ''' test user can get all meetup records '''
        
        response = self.client.get(self.get_url,content_type = "application/json",headers=self._get_header())
        self.assertEqual(response.status_code, 200)

    def test_user_can_get_specific_meetup_record(self):
        ''' test whether user can get a specific record using it's meetup id '''

        self.client.post(self.post_url, data = json.dumps(self.meetups[0]), content_type="application/json",headers=self._get_header())
        self.client.post('api/v1/meetups/', data = json.dumps(self.meetups[1]), content_type="application/json",headers=self._get_header())

        response = self.client.get(self.get_url, content_type="application/json",headers=self._get_header())
        result = json.loads(response.data.decode('UTF-8'))
        self.assertEqual(response.status_code,200)
        self.assertEqual(result["topic"],"Ethical Hacking Hackathon")

    def test_rsvp_meetup(self):
        ''' tests whether user can respond to a meeting invitation '''

        rsvp_url ='api/v1/meetups/1/rsvps'

        # post two meetup records
        self.client.post('api/v1/meetups/', data = json.dumps(self.meetups[0]), content_type="application/json",headers=self._get_header())
        self.client.post('api/v1/meetups/', data = json.dumps(self.meetups[1]), content_type="application/json",headers=self._get_header())
        self.client.post('api/v1/meetups/', data = json.dumps(self.meetups[1]), content_type="application/json",headers=self._get_header())
        
        response = self.client.post(rsvp_url,data=json.dumps(self.rsvp) ,content_type="application/json",headers=self._get_header())
        result = json.loads(response.data.decode('UTF-8'))
        self.assertEqual(response.status_code,201)
        self.assertEqual(result["data"]['status'],'yes')

if __name__ == "__main__":
    unittest.main()
   

    