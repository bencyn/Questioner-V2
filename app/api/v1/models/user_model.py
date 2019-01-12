from datetime import datetime

users = []

logged_in_users = []

class User(object):
    """ user class """

    def __init__(self):
        self.users = users

    def create_user(self,firstname,lastname,othername,email,phoneNUmber,username,registered,isAdmin):
        """ create a user account"""
        
        user = {
            "id" : len(self.users)+ 1,
            "firstname" :firstname,
            "lastname": lastname,
            "othername" : othername,
            "email" : email,
            "phoneNumber" : phoneNUmber,
            "username" : username,
            "registered" :registered,
            "isAdmin" :isAdmin,
            "createdOn":datetime.now()
        }
        self.users.append(user)

        return user

    def login_user(self,username,password):
        """ login a user after validation """

        token = ''

        user = {
            "username":username,
            "password":password,
            "token":token

        }

    def get_users(self):
        return self.users

    def get_user(self,id):
        for user in users:
            if user["id"] == id:
                return user

    def authenticate_user(self):
        pass