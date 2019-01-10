from datetime import datetime

meetup = []

class Meetup(object):
    """ meetups class """

    def __init__(self):
        self.meetups = meetup

    def add_meetup(self,location, images, topic,happeningOn, tags):
        """ creates a meetup record"""
        createdOn = datetime.now()
        
        meetup = {
            "id": len(self.meetups) + 1,
            "topic": topic,
            "location": location,
            "createdOn": createdOn,
            "images": images,
            "happeningOn": happeningOn,
            "tags": tags,
        }   

        self.meetups.append(meetup)
        return meetup

    def get_meetups(self):
        return self.meetups

    def get_meetup(self,id):
        return self.meetups[id]