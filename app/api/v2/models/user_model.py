from datetime import datetime

users = []
logged_in_users = []

class User(object):
    """ user class """

    def __init__(self):
        """initialize and define objects """
        self.users = users
        self.logged_in_user = logged_in_users

    def create_user(self,firstname,lastname,othername,email,password,phoneNUmber,username,isAdmin):
        """ create a user account"""
        #  user = user_object.create_user(firstname,lastname,othername,email,password,phoneNUmber,username,isAdmin)
        
        user = {
            "id" : len(self.users)+ 1,
            "firstname" :firstname,
            "lastname": lastname,
            "othername" : othername,
            "email" : email,
            "phoneNumber" : phoneNUmber,
            "username" : username,
            "password":password,
            "registered" :datetime.now(),
            "isAdmin" :isAdmin
        }
        self.users.append(user)

        return user

    def login_user(self,username,password,token):
        """ login a user after validation """
        
        user = {
            "username":username,
            "password":password,
            "token":token,
        }
        
        self.logged_in_user.append(user)
        return user

    def get_users(self):
        """ get all registered users """
        return self.users

    def get_user(self,id):
        """ get user by id """
        for user in users:
            if user["id"] == id:
                return user

