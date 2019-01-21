import psycopg2, os
from psycopg2.extras import RealDictCursor
from app.database.connect import db_init
from flask import Flask, json, jsonify

class BaseModel:
    """ defines global functions for sub models """

    def __init__(self):
        """ initialize database """
        self.conn =db_init()
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)

    def save_data(self,sql,**kwargs):
        """save queries"""
        self.conn = db_init()
        cur=self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        try:
            cur.execute(sql)
        except psycopg2.DatabaseError as e:
            message = {'message': '{}'.format(e)}
            return jsonify({"status": 400,"error":message}), 400

        result = cur.fetchone()[0]
        self.conn.commit()
        cur.close()
        return jsonify({"status": 201,
                        "message":"username {} registered successfully".format(result),
                        "token":kwargs['token']
                    }), 201
  
    def check_if_exists(self, table, field, data):
        """ check if a record or records exist """
        self.conn = db_init()
        cur=self.conn.cursor()
        query = "SELECT * FROM {} WHERE {}='{}'".format(table, field, data)
        # return cur.fetchone() is not None
        cur.execute(query)
        if cur.fetchone():
            return True
        else:
            return False
    
    def get_user_by_username(self,username):
        """ get user by username """
        
        self.conn = db_init()
        cur=self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        self.username =username
        query="""SELECT username, password FROM users WHERE username = '{}'""".format(self.username)
        cur.execute(query)
        data = cur.fetchone()
        cur.close()

        return data

    def get_all(self,table):
        """ get all records"""
        self.conn = db_init()
        table = "users"
        cur=self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query="""SELECT * FROM {} """.format(table)
        cur.execute(query)
        self.data = cur.fetchall()
        cur.close()
        result = []
        for row in self.data:
            result.append(dict(row))
        return result

    def get_record_by_id(self,table,field,value):
        """ get records  by id"""
        self.conn = db_init()
        cur=self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        value = int(value)
        query = """SELECT * FROM users WHERE users.id=%d;"""%(value)
        cur.execute(query)
        data= cur.fetchone()
        cur.close()
        result = []
        result.append(dict(data))
        if not data:
            return jsonify({"status": 400,"error":"no data record found"}), 400
        else:
            return result

    def execute_query(self,query):
        self.conn = db_init()
        cur=self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
    
    def call_cursor(self):
        pass