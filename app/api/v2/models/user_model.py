from datetime import datetime
import psycopg2, os
from app.database.connect import db_init
from flask import Flask, json, jsonify
from .base_model import BaseModel


class User(BaseModel):
    """ user class """

    def __init__(self):
        """initialize and define objects """
        pass

    def create_user(self,**kwargs):
        """ create a user account in users table """
        
        self.firstname= kwargs['firstname']
        self.lastname= kwargs['lastname']
        self.othername= kwargs['othername']
        self.email= kwargs['email']
        self.phone_number= kwargs['phone_number']
        self.username= kwargs['username']
        self.password= kwargs['password']
        self.registered= str(datetime.now())
        self.is_admin=kwargs.get('is_admin','0')

        sql = """ INSERT INTO users (firstname,lastname,othername,email,phone_number,username,password,is_admin)
                VALUES('{}','{}','{}','{}','{}','{}','{}','{}') RETURNING users.username;""".format(self.firstname,self.lastname,self.othername,self.email,self.phone_number,self.username,
                                    self.password,self.is_admin)

        check_username = self.check_if_exists("users","username",self.username)
        check_email = self.check_if_exists("users","email",self.email)

        if check_username:
            return jsonify({
                "status": 400,
                "error": "{} already exists".format("username")
            }), 400
        elif check_email:
            return jsonify({
                "status": 400,
                "error": "{} already exists".format("email")
            }), 400
        else:
            save_user=self.save_data(sql,**kwargs)
            return save_user
   
    def login_user(self):
        """"""
        pass
    # def get_user_by_id(self,id):
    #     self.id =id
    #     cur=conn.cursor()
    #     query="""SELECT * FROM users WHERE id ={}""".format(self.id)
    #     cur.execute(query)
    #     self.user=cur.fetchall()
    #     # curr.close()
    
    #     return self.user
