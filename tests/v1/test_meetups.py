import json ,unittest,instance,datetime
from .base_tests import BaseTest
from app.v1.models.meetup_model import Meetup
from app.v1.views import meetup_view
from app.v1.models import meetup_model
from app import create_app

app = create_app("testing")

class TestUser(BaseTest):
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

        self.meetup1 = {
                "id":1,
                "createdOn":"Wed,10 Jan 2019",
                "location":"Nakuru",
                "images":["img1.png","img2.png"],
                "topic":"empowering local talent",
                "happeningOn":"Friday, 20 Feb 2019",
                "Tags":['dunda','gospel','reggae']
            }
        self.meetup2 = {
                "id":2,
                "createdOn":"Fri,10 Jan 2019",
                "location":"Nyahururu",
                "images":["img1.png","img2.png"],
                "topic":"Antivals Hackathon",
                "happeningOn":"Friday, 28 Feb 2019",
                "Tags":['startup','innovation','passion']
        }
        self.meetups = [{
                "id":1,
                "createdOn":"Wed,10 Jan 2019",
                "location":"Nakuru",
                "images":["img1.png","img2.png"],
                "topic":"empowering local talent",
                "happeningOn":"Friday, 20 Feb 2019",
                "Tags":['dunda','gospel','reggae']
            },
            {
                "id":2,
                "createdOn":"Fri,10 Jan 2019",
                "location":"Nyahururu",
                "images":["img1.png","img2.png"],
                "topic":"Antivals Hackathon",
                "happeningOn":"Friday, 28 Feb 2019",
                "Tags":['startup','innovation','passion']
            }
        ]

    # def test_meeetup_create_record(self):
    #         ''' test user can create a meetup record'''
    #         url = 'api/v1/meetups'
    #         response= self.client.post(url, json.dumps(self.meetup), content_type="application/json")
    #         result = json.loads(response.data.decode('UTF-8'))

    #         self.assertEqual(response.status_code, 201)
    #         self.assertEqual(result["status"], 201)
    #         self.assertEqual(result["data"], [
    #             {
    #                 "createdOn":datetime.datetime.now(),
    #                 "topic": "Python",
    #                 "location": "Nairobi",
    #                 "happeningOn": "Thursday",
    #                 "tags": ["RESTful API", "JSON Data"],
    #             }
    #         ])

    def test_user_can_get_meetup_records(self):
            ''' test user can get all meetup records '''

            url = 'api/v1/meetups/upcoming/'
            response = self.client.get(url,content_type = "application/json")
            self.assertEqual(response.status_code, 200)


    # def test_get_meetup_specific_record(self):
    #         '''test user can get a specific record using meetup'''

    #         url = 'api/v1/meetups/2'

    #         self.client.post("api/v1/meetups", json.dumps(self.meetup1), content_type = "application/json")
    #         self.client.post("api/v1/meetups", json.dumps(self.meetup2),  content_type = "application/json")

    #         response = self.client.get(url, content_type = "application/json")
    #         self.assertEqual(response.status_code, 200)

    #         result = json.loads(response.data.decode('utf-8'))
    #         self.assertEqual(result['status'], 200)
    #         self.assertEqual(result['data'], [{
    #                                         "id":2,
    #                                         "createdOn":"Fri,10 Jan 2019",
    #                                         "location":"Nyahururu",
    #                                         "images":["img1.png","img2.png"],
    #                                         "topic":"Antivals Hackathon",
    #                                         "happeningOn":"Friday, 28 Feb 2019",
    #                                         "Tags":['startup','innovation','passion']
    #                                         }])

if __name__ == "__main__":
    unittest.main()
   

    