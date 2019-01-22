import psycopg2
from psycopg2.extras import RealDictCursor
from app.database import migrations

class Connection:
    """Initializees the database"""

    def __init__(self):
        self.app = None
        self.connection = None
        self.cursor = None
        
    def init_db(self,app):
        """Initializes the database connection"""
        self.app = app
        url =app.config.get("DATABASE_URL")
        self.connection = psycopg2.connect(url)
        # self.connection = psycopg2.connect(dbname=app.config.get("DATABASE_NAME"), user=app.config.get("DATABASE_USER"), password=app.config.get("DATABASE_PASSWORD"),port='5432', host=app.config.get("DATABASE_HOST"))
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def create_tables(self):
        """create tables in the database"""
        tables = migrations.tables()
        try:
            for query in tables:
                self.cursor.execute(query)
            self.connection.commit()
        except:
            print("Fail")
    

    def drop_tables(self):
        """destroy test database """
        queries = migrations.tables_to_drop()
        try:
            for query in queries:
                self.cursor.execute(query)
                self.connection.commit()
        except:
            print("Fail")