from flask import Flask, json, jsonify, request, make_response, Blueprint
from datetime import datetime
from ..models import meetup_model

meetup = Blueprint('meetup', __name__, url_prefix='/api/v1/meetups')
meetup_object = meetup_model.Meetup()

@meetup.route("/upcoming/", methods=['GET'])
def getMeetups():
    ''' fetch all meetup records'''
    return jsonify(meetup_object.get_meetups()),200


@meetup.route("/<int:id>", methods = ['GET'])
def getMeetup(id):
    ''' get a specific meetup'''
    return jsonify(meetup_object.get_meetup(id)),200
    # return jsonify(meetup)


@meetup.route('/', methods = ['POST'])
def create_meetup():
    '''endpoint to create a meetup record'''
    data = request.get_json()

    topic = data.get('topic')
    location = data.get('location')
    images = data.get('images')
    happeningOn = data.get('happeningOn')
    tags = data.get('tags')
    
    if not topic:
        return validate_input("topic")
    if not location:
        return validate_input("location")
    if not happeningOn:
        return validate_input("happeningOn")
    if not tags:
        return validate_input("tags")
    if not images:
        return validate_input("images")
    else:
        meetup = meetup_object.add_meetup(location,images,topic,happeningOn,tags)
        return jsonify({
            "status": 201,
            "data":meetup
        }), 201

@meetup.route("/<int:meetup_id>/rsvps", methods = ['POST'])
def rsvpMeetup(meetup_id):
    """ meetup reserve method """

    try:
        status = request.get_json()['status']
    except KeyError:
        return jsonify({'status': 400,
                        ' error': "rsvps data required"})
    if not status:
        return validate_input("rsvps status")

    else:
        meetups = meetup_object.meetups
        if meetups:
            rsvps_meetup = meetups[meetup_id]
            topic=rsvps_meetup["topic"]
    
            return make_response(jsonify({
                "status":201,
                "data":{
                    "topic":topic,
                    "status":status,
                }
            })), 201

        return jsonify({"status": 404, "error": "Meetup not found"}), 404
  
  

@meetup.route("/<meetup_id>/rsvps", methods = ['POST'])
def reserveMeetup(meetup_id):
    """ meetup reserve logic """
    data = request.get_json()
    try:
        status = data.get('status')
    except KeyError:
        return jsonify({'status': 400,
                        ' error': "rsvps data required"})
    if not status:
        return validate_input("rsvps status")
    else:
        meetups = meetup_object.meetups
        if meetup:
            rsvps_meetup = meetups[meetup_id]
            topic=rsvps_meetup["topic"]
    
            return make_response(jsonify({
                "status":201,
                "data":{
                    "topic":topic,
                    "status":status,
                }
            })), 201

        return jsonify({"status": 404, "error": "Meetup not found"}), 404
  
  

def validate_input(field):
     return make_response(jsonify({
            "status": 400,
            "message": "{} cannot be empty".format(field)
        })), 400
