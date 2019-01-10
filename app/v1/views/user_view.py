from flask import Flask, json, jsonify, request, make_response, Blueprint
from datetime import datetime
# from ..models import user_model
from app.v1.models import user_model

user = Blueprint('meetup', __name__, url_prefix='/api/v1/users')
user_object = user_model.User()


@user.route("/all", methods=['GET'])
def getUsers():
    ''' fetch all user recorce'''
    return jsonify(user_object.get_users()),200


# user signup and get users
@user.route("/create", methods=['POST'])
def register():
    """user signup"""
    data = request.get_json()

    if not data:
        return jsonify({"Message": 'Cannot send empty data'})
    if not all(field in data for field in ['username', 'email','password']):
        return jsonify({"Message": "All fields are required"})
    
    firstname = request.get_json()['firstname']
    lastname = request.get_json()['lastname']
    othername = request.get_json()['othername']
    email = request.get_json()['email']
    phoneNUmber = request.get_json()['phoneNUmber']
    password = request.get_json()['password']
    username = request.get_json()['username']
    isAdmin = request.get_json()['isAdmin']
 
    if not firstname:
        return validate_input("firstname")
    if not lastname:
        return validate_input("lastname")
    if not othername:
        return validate_input("othername")
    if not email:
        return validate_input("email")
    if not phoneNUmber:
        return validate_input("phoneNUmber")
    if not password:
        return validate_input("password")
    if not username:
        return validate_input("username")
    
    
    if any(i['username'] == username for i in user_object.users):
        return jsonify({'msg': 'username already exists'}), 409
    if any(i['email'] == email for i in user_object.users):
        return jsonify({'msg': 'email already exists'}), 409
    else:
        # add create user
        user_object.create_user(firstname,lastname,othername,email,password,phoneNUmber,username,isAdmin)
        return jsonify({'user': user}), 201

def validate_input(field):
     return make_response(jsonify({
            "status": 400,
            "message": "{} cannot be empty".format(field)
        })), 400
