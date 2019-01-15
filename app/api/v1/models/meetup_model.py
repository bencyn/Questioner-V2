from datetime import datetime

meetups = []

class Meetup(object):
    """ meetups class """

    def __init__(self):
        """ initialize and define meetup objects"""
        self.meetups = meetups

    def add_meetup(self,args):
        """ creates a meetup record"""
        createdOn = datetime.now()
        
        meetup = {
            "id": len(self.meetups) + 1,
            "topic": args["topic"],
            "location": args["location"],
            "createdOn": createdOn,
            "images": args["images"],
            "happeningOn": args["happeningOn"],
            "tags": args['tags'],
        }   

        self.meetups.append(meetup)
        return meetup

    def get_meetups(self):
        """ return all meetup records """
        return self.meetups

    def get_meetup(self,id):
        '''' get meetup record by id '''
        for meetup in self.meetups:
            if meetup["id"] == id:
                return meetup