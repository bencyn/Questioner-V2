# import psycopg2, os
# from app.database.connect import db_init
from flask import Flask, json, jsonify
from .base_model import BaseModel


class Meetup(BaseModel):
    """ meetup class """

    def __init__(self):
        """initialize and define objects """
        super().__init__()
    def create_meetup(self,**kwargs):
        """ create a meetup record """
        self.topic= kwargs['topic']
        self.location= kwargs['location']
        self.images= kwargs['images']
        self.happening_on= kwargs['happening_on']
        self.tags= kwargs['tags']
        self.user_id= kwargs['user_id']
        

        sql = """ INSERT INTO meetups (happening_on,location,images,topic,tags,user_id)
                VALUES('{}','{}','{}','{}','{}','{}') RETURNING meetups.id;""".format(self.happening_on,self.location,self.images,self.topic,
                self.tags,self.user_id)

        save_meetup=self.save_data(sql)
        meetup = self.get_by_key("meetups","id",save_meetup["id"])
        return meetup
   
    def login_user(self):
        """"""
        pass
  