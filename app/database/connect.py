import psycopg2 ,os
from flask import current_app
from app.database import migrations

class Connection:

    def __init__(self):
        pass

    def connect_db(self,url):
        """ initiate a database connection"""
        try:
            self.conn = psycopg2.connect(url)
            return self.conn
        except psycopg2.DatabaseError as e:
            return {'message': '{}'.format(e)}

    def db_init(self):
        """ setup database """
        # url = current_app.config['DATABASE_URL']
        url = os.getenv('DATABASE_URL')
        self.conn = self.connect_db(url)
        self.create_tables(self.conn)
        return self.conn

    def test_db_init(self):
        """" setup database in test environment """

        url = os.getenv('TEST_DATABASE_URL')
        self.conn = self.connect_db(url)
        self.create_tables(self.conn)
        self.conn.commit()
        return self.conn

    def create_tables(self,conn):
        """create tables in the database"""
        curr = conn.cursor()
        tables = migrations.tables()

        for query in tables:
            curr.execute(query)
        conn.commit()
        

    def drop_tables(self):
        """destroy test database """
        test_url = os.getenv('TEST_DATABASE_URL')
        conn = self.connect_db(test_url)
        curr = conn.cursor()
        queries = migrations.tables_to_drop()
        try:
            for query in queries:
                curr.execute(query)
            conn.commit()
        except:
            print("Fail")
