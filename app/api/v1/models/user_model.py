from datetime import datetime

users = []
logged_in_users = []

class User(object):
    """ user class """

    def __init__(self):
        """initialize and define objects """
        self.users = users
        self.logged_in_user = logged_in_users

    def create_user(self,**kwargs):
        """ create a user account"""
        user = {
            "id" : len(self.users)+ 1,
            "firstname" :kwargs['firstname'],
            "lastname": kwargs['lastname'],
            "othername" : kwargs['othername'],
            "email" :kwargs['email'],
            "phone_number" :  kwargs['phone_number'],
            "username" : kwargs['username'],
            "password":kwargs['password'],
            "registered" :datetime.now(),
            "isAdmin" :kwargs.get('is_admin','0')
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

