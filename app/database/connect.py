import psycopg2 ,os
from flask import current_app
from app.database import migrations

def connect_db(url):
    """ initiate a database connection"""
    try:
        conn = psycopg2.connect(url)
        return conn
    except psycopg2.DatabaseError as e:
        return {'message': '{}'.format(e)}

def db_init():
    """ setup database """
    url = current_app.config['DATABASE_URL']
    conn = connect_db(url)
    create_tables(conn)
    return conn

def test_db_init():
    """" setup database in test environment """

    url = os.getenv('TEST_DATABASE_URL')
    conn = connect_db(url)
    create_tables(conn)
    return conn

def create_tables(conn):
    """create tables in the database"""
    curr = conn.cursor()
    tables = migrations.tables()

    for query in tables:
        curr.execute(query)
    conn.commit()
    

def drop_tables():
    """destroy test database """
    test_url = os.getenv('TEST_DATABASE_URL')
    conn = connect_db(test_url)
    curr = conn.cursor()
    queries = migrations.tables_to_drop()
    try:
        for query in queries:
            curr.execute(query)
        conn.commit()
    except:
        print("Fail")