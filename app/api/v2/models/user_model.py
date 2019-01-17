from datetime import datetime


class User(object):
    """ user class """

    def __init__(self):
        """initialize and define objects """


    def create_user(self,firstname,lastname,othername,email,password,phoneNUmber,username,isAdmin):
        """ create a user account"""
        #  user = user_object.create_user(firstname,lastname,othername,email,password,phoneNUmber,username,isAdmin)
        
        user = {
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

        return user

    def login_user(self,username,password,token):
        """ login a user after validation """
        
        user = {
            "username":username,
            "password":password,
            "token":token,
        }
        
        return user

    def get_users(self):
        """ get all registered users """
        pass
        # return self.users

    def get_user(self,id):
        """ get user by id """
        pass
        # for user in users:
        #     if user["id"] == id:
        #         return user

