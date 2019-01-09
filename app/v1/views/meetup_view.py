from flask import Flask, json, jsonify, request, make_response, Blueprint
from datetime import datetime
from ..models import meetup_model

meetup = Blueprint('meetup', __name__, url_prefix='/api/v1/meetup')
meetup_object = meetup_model.Meetup()


@meetup.route('/create', methods = ['POST'])
def create_meetup():
    '''endpoint to create a meetup'''
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
        return make_response(jsonify({
            "status": 201,
            "data":meetup
        })), 201

def validate_input(field):
     return make_response(jsonify({
            "status": 400,
            "message": "{} cannot be empty".format(field)
        })), 400
