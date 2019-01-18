from psycopg2.extras import RealDictCursor
from app.database.connect import db_init

class BaseModel(object):
    """ defines global functions for sub models """

    def __init__(self):
        """ initialize database """
        self.conn =db_init()
        # self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        self.cursor =db_init().cursor()
    def check_if_exists(self, table, field, data):
        """ check if a record or records exist """
        curr = db_init().cursor()
        query = "SELECT * FROM {} WHERE {}='{}'".format(table, field, data)
        curr.execute(query)
        # self.cursor.execute(query)
        # if self.cursor.fetchone() is not None:
        if curr.fetchone() is not None:
            return True
        else: 
            return False