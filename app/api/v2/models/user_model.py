from datetime import datetime
from .base_model import BaseModel
from app.database.connect import db_init
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
        self.phoneNumber= kwargs['phoneNumber']
        self.username= kwargs['username']
        self.password= kwargs['password']
        self.registered= datetime.now()
        self.isAdmin=kwargs.get('isAdmin','0')
        user ={"firstname":self.firstname,"lastname":self.lastname,"othername":self.othername,"email":self.email,
                "phoneNumber":self.phoneNumber,"username":self.username,"password":self.password,"isAdmin":self.isAdmin,}

        # check if user exists
        if self.check_if_exists(table="users", field="username", data=self.username):
            return False
        
        curr = db_init().cursor()
        query = """ INSERT into users (firstname,lastname,othername,phoneNumber,username,
            password,registered,isAdmin) values('{}', '{}', '{}', '{}','{}', '{}', '{}', '{}') RETURNING users.id 
            """.format(self.firstname, self.lastname, self.othername,self.phoneNumber,self.username, 
                    self.password,self.registered,self.isAdmin)

        # self.cursor.execute(query)
        curr.execute(query)
        # self.conn.commit(),
        db_init().commit()
        # self.user = self.cursor.fetchone()[0]
        self.user =curr.fetchone()[0]
        # self.cursor.close()
        curr.close()
        return self.user

    def get_user_by_username(self,username):
        """ get username by username """
        self.username =username
        curr = db_init().cursor()
        query="""SELECT username, password FROM users WHERE username = '{}'""".format(self.username)
        curr.execute(query)
        self.user = curr.fetchone()
        curr.close()
    
        return self.user

    def get_user_by_id(self,id):
        self.id =id
        curr = db_init().cursor()
        query="""SELECT * FROM users WHERE id = '{}'""".format(self.id)
        curr.execute(query)
        self.user = curr.fetchone()
        curr.close()
    
        return self.user