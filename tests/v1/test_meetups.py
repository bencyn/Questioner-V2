import json ,unittest,instance,datetime
from .base_tests import BaseTest
from app import create_app

app = create_app("testing")

class TestMeetup(BaseTest):
    def setUp(self):
        """ defining test data"""
        app.config.from_object(instance.config.TestingConfig)
        self.client = app.test_client()

        self.meetup = {
            "topic": "Ethical Hacking Hackathon",
            "location": "Nairobi",
            "images": ["image3.png", "image4.png"],
            "happeningOn": "Monday 12 2018",
            "tags": ["Pentests", "Bruteforce"]
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
                "tags": ["Pentests", "Bruteforce"],
                "images":"https://bencyn.github.io/Questioner/UI/images/456470.jpeg,https://bencyn.github.io/Questioner/UI/images/475058220.jpeg"
            
            }]
        self.rsvp={"status":"yes"}
        self.get_url = 'api/v1/meetups/2'
        self.post_url ='api/v1/meetups/'

    def test_user_can_create_meeetup_record(self):
        with self.client:
            ''' test user can create a meetup record'''
            # url = api/v1/meetups/
            response= self.client.post('api/v1/meetups/', data = json.dumps(self.meetups[0]), content_type="application/json")
          
            self.assertEqual(response.status_code, 201)
   
    def test_user_can_get_meetup_records(self):
        ''' test user can get all meetup records '''
        
        response = self.client.get(self.get_url,content_type = "application/json")
        self.assertEqual(response.status_code, 200)

    def test_user_can_get_specific_meetup_record(self):
        ''' test whether user can get a specific record using it's meetup id '''

        self.client.post(self.post_url, data = json.dumps(self.meetups[0]), content_type="application/json")
        self.client.post('api/v1/meetups/', data = json.dumps(self.meetups[1]), content_type="application/json")

        response = self.client.get(self.get_url, content_type="application/json")
        self.assertEqual(response.status_code,200)

    def test_rsvp_meetup(self):
        ''' tests whether user can respond to a meeting invitation '''

        rsvp_url ='api/v1/meetups/1/rsvps'

        # post two meetup records
        self.client.post('api/v1/meetups/', data = json.dumps(self.meetups[0]), content_type="application/json")
        self.client.post('api/v1/meetups/', data = json.dumps(self.meetups[1]), content_type="application/json")
        
        response = self.client.post(rsvp_url,data=json.dumps(self.rsvp) ,content_type="application/json")
        result = json.loads(response.data.decode('UTF-8'))
        self.assertEqual(response.status_code,201)
        self.assertEqual(result["data"]['status'],'yes')
        # self.assertEqual(response)

if __name__ == "__main__":
    unittest.main()
   

    