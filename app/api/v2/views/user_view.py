from flask import Flask, json, jsonify, request, make_response, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import app,re
from app.api.v2.models import user_model
from ..utils.validators import Validators

user_v2 = Blueprint('user_v2', __name__, url_prefix='/api/v2/auth')
auth_v2 = Blueprint('auth_v2',__name__, url_prefix='/api/v2/auths')

user_object = user_model.User()
validator = Validators()

@user_v2.route("/all", methods=['GET'])
@app.jwt_required
def getUsers():
    ''' this endpoints allows a user to fetch all registered users'''
    users = user_object.get_all("users")
    return jsonify({
        "status":200,
        "users":users
    }),200

@user_v2.route("/<int:id>", methods = ['GET'])
@app.jwt_required
def getUser(id):
    ''' this endpoints allow a user to get a specific user by id'''
    # id = str(id)
    user =user_object.get_record_by_id("users","id",id)
    return jsonify({
        "status":200,
        "user":user
    }),200
   

@user_v2.route('/signup', methods = ['POST'])
def register():
    """ this endpoint allows unregistered users to signup """
    data = request.get_json()

    if not data:
        return jsonify({"Message": 'Cannot send empty data'}),409
    
    firstname = request.get_json()['firstname']
    lastname = request.get_json()['lastname']
    othername = request.get_json()['othername']
    email = request.get_json()['email']
    phone_number = request.get_json()['phone_number']
    password = request.get_json()['password']
    username = request.get_json()['username']
    is_admin = request.get_json()['is_admin']

    val_input = {"username":username,"email":email,"password":password}

    for key,value in val_input.items():
        if not value.strip():
            return make_response(jsonify({
                "status": 400,
                "error": "{} cannot be empty".format(key)
            })), 400
            
        if key == "email":
            if  not re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                                value):
                return jsonify({'status': 400,
                            'error': "email provided is invalid"}),400

    passwordHash = generate_password_hash(password)
    access_token = app.create_access_token(identity=username)
    user_details ={"firstname":firstname,"lastname":lastname,"othername":othername,"email":email,
                "phone_number":phone_number,"username":username,"password":passwordHash,"is_admin":is_admin,"token":access_token}
    
    user =user_object.create_user(**user_details)
    return user
 


@user_v2.route('/login', methods = ['POST'])
def login():
    """ this endpoint allows a user to login and auto-generate an auth token """

    if not request.data:
        return validator.validate_missing_data()

    username = request.get_json()['username']
    password = request.get_json()['password']
    
    val_input = {"username":username,"password":password}

    for key,value in val_input.items():
        if not value.strip():
            return make_response(jsonify({
                "status": 400,
                "error": "{} cannot be empty".format(key)
            })), 400

    user = user_object.get_user_by_username(username)
    
    if user:
        validate_password = check_password_hash(user["password"], password)
        if validate_password:
            jwt_token = app.create_access_token(identity=username)
            return jsonify({ 
                "status": 201,
                "data":[{
                    "token":jwt_token,
                    "user":user
                }],
                "message":"user logged in successfully",
            }), 201
        return jsonify({'msg': 'incorrect username/password combination' }), 401
    else:
        return jsonify({'msg': 'user does not exist' }), 404


@auth_v2.route('/token', methods=['GET'])
@app.jwt_required
def protected():
    """ access identity of the current user """
    current_user = app.get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

