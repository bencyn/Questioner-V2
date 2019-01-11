from flask import Flask, json, jsonify, request, make_response, Blueprint
from datetime import datetime
# from ..models import user_model
from app.api.v1.models import user_model

user = Blueprint('user', __name__, url_prefix='/api/v1/users')
user_object = user_model.User()


@user.route("/all", methods=['GET'])
def getUsers():
    ''' fetch all users'''
    return jsonify(user_object.get_users()),200

@user.route("/<int:id>", methods = ['GET'])
def getMeetup(id):
    ''' get a specific meetup'''
    return jsonify(user_object.get_user(id)),200

@user.route('/', methods = ['POST'])
def register():
    """user signup"""
    data = request.get_json()

    if not data:
        return jsonify({"Message": 'Cannot send empty data'}),409
    
    firstname = request.get_json()['firstname']
    lastname = request.get_json()['lastname']
    othername = request.get_json()['othername']
    email = request.get_json()['email']
    phoneNUmber = request.get_json()['phoneNUmber']
    password = request.get_json()['password']
    username = request.get_json()['username']
    isAdmin = request.get_json()['isAdmin']

    if not username:
        return validate_input("username")
    if not email:
        return validate_input("email")
    if not password:
        return validate_input("password")
    else:
        # add create user
        user = user_object.create_user(firstname,lastname,othername,email,password,phoneNUmber,username,isAdmin)
        return jsonify({
            "status": 201,
            "data":user
        }), 201

def validate_input(field):
     return make_response(jsonify({
            "status": 400,
            "message": "{} cannot be empty".format(field)
        })), 400

