import psycopg2 ,os
from flask import current_app
from app.database import migrations

def connect_db(url):
    """ initiate a database connection"""

    url = current_app.config.get('DATABASE_URL')
    try:
        conn = psycopg2.connect(url)
        return conn
    except psycopg2.DatabaseError as e:
        return {'message': '{}'.format(e)}

def db_init():
    """ setup database connection """
    url = current_app.config['DATABASE_URL']
    conn = psycopg2.connect(url)
    return conn

def test_db_init():
    """" setup database in test environment """

    url = current_app.config['DATABASE_URL']
    conn = connect_db(url)
    curr = conn.cursor()
    tables = migrations.tables()

    for query in tables:
        curr.execute(query)
    conn.commit()
