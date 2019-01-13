from flask import Flask, json, jsonify, request, make_response, Blueprint
from datetime import datetime
# from flask_jwt_extended import (
#     JWTManager,jwt_manager, create_access_token,get_jwt_identity
# )
# get user model
from app.api.v1.models import user_model
from ..utils.validators import Validators
import app

user = Blueprint('user', __name__, url_prefix='/api/v1/users')
user_object = user_model.User()
validator = Validators()


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
        return validator.validate_input("username")
    if not email:
        return validator.validate_input("email")
    if not password:
        return validator.validate_input("password")
    else:
        # add create user
        user = user_object.create_user(firstname,lastname,othername,email,password,phoneNUmber,username,isAdmin)
        
        return jsonify({
            "status": 201,
            "data":user
        }), 201

@user.route('/login', methods = ['POST'])
def login():
    if not request.data:
        return validator.validate_missing_data()

    username = request.get_json()['username']
    password = request.get_json()['password']
    
    if not username:
        return validator.validate_input("username")
    if not password:
        return validator.validate_input("password")
    else:
        # check  if user exists return 401 unauthorized error
        users = user_object.users
        if any(y['username'] == username for y in users) and any(y['password'] == password for y in users):
                # generate token
            access_token = app.create_access_token(identity=username)
            user_loggedIn = user_object.login_user(username,password,access_token)
            
            return jsonify({
                "status": 201,
                "message":"user logged in successfully",
                "data":user_loggedIn
            }), 201
        else:
            return jsonify({'msg': 'incorrect username/password combination' }), 401


