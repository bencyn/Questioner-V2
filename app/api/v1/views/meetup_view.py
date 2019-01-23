from flask import Flask, json, jsonify, request, make_response, Blueprint
from datetime import datetime
from ..models import meetup_model
import app

meetup = Blueprint('meetup', __name__, url_prefix='/api/v1/meetups')
meetup_object = meetup_model.Meetup()

@meetup.route("/upcoming/", methods=['GET'])
@app.jwt_required
def getMeetups():
    ''' fetch all meetup records'''
    return jsonify(meetup_object.get_meetups()),200

@meetup.route("/<int:id>", methods = ['GET'])
@app.jwt_required
def getMeetup(id):
    ''' this function gets a  specific meetup by id'''
    return jsonify(meetup_object.get_meetup(id)),200

@meetup.route('/', methods = ['POST'])
@app.jwt_required
def create_meetup():
    '''this endpoints allows users to create a meetup record '''

    data = request.get_json()

    if not data:
        return jsonify({"Message": 'Cannot send empty data'}),409
    else:
        topic = data.get('topic')
        location = data.get('location')
        images = data.get('images')
        happeningOn = data.get('happeningOn')
        tags = data.get('tags')
        
        val_input = {"topic":topic,"location":location,"happeningOn":happeningOn,"tags":tags}

        for key,value in val_input.items():
            if  not value.strip() :
                return make_response(jsonify({
                    "status": 400,
                    "error": "{} cannot be empty".format(key)
                })), 400
                
        # pass user input
        user_input = {"topic":topic,"location":location,"images":images,"happeningOn":happeningOn,"tags":tags}
        meetup = meetup_object.add_meetup(**user_input)
        return jsonify({"status": 201,"data":meetup}), 201

@meetup.route("/<int:meetup_id>/rsvps", methods = ['POST'])
@app.jwt_required
def reserveMeetup(meetup_id):
    """ this endpoint allows a user to submit a meetup reserve response """

    data = request.get_json()
    try:
        status = data.get('status')
    except KeyError:
        return jsonify({'status': 400,
                        ' error': "rsvps data required"})

    if not status.strip():
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
    """ returns an empty error message"""

    return make_response(jsonify({
        "status": 400,
        "message": "{} cannot be empty".format(field)
    })), 400
