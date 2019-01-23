from datetime import datetime
from flask import Flask, json, jsonify
from .base_model import BaseModel

class Question(BaseModel):
    """ questions class """
    def __init__(self):
        """initialize and define objects """
        super().__init__()
       
    def create_question(self,**kwargs):
        """" defines the logic for adding a question """
        #  question_details = {"title":title,"body":body,"meetup_id":meetup_id,"user_id":user_id}
        self.title= kwargs['title']
        self.body= kwargs['body']
        self.meetup_id= kwargs['meetup_id']
        self.user_id= kwargs['user_id']
        self.votes =int(x=0)

        check_user = self.check_if_exists("users","id",self.user_id)
        check_meetup = self.check_if_exists("meetups","id",self.meetup_id)

        if not check_user:
            return jsonify({
                "status": 404,
                "error": "{} not found".format("user")
            }), 404
        elif not check_meetup:
            return jsonify({
                "status": 404,
                "error": "{} not found".format("meetup record")
            }), 404
        else:
            #  id | meetup_id | user_id | created_by | title | body | votes | created_on 
    
            sql = """ INSERT INTO questions (meetup_id,created_by,title,body,votes)
                VALUES({},{},'{}','{}','{}') RETURNING questions.id;""".format(self.meetup_id,self.user_id,
                    self.title,self.body,self.votes)
            save_question=self.save_data(sql)
            question =self.get_by_key("questions","id",save_question["id"])
            return jsonify({"status": 201,
                    "question":question,
                    "message":"question posted successfully",
            }), 201

    def get_question(self,id):
        ''' get question by key id '''
        pass
        # for question in questions:
        #     if question["id"]==id:
        #         return question

    def upvote_question(self,**kwargs):

        self.username=kwargs['username']
        self.question_id=kwargs['question_id']
        self.vote =1

        user = self.get_by_key("users","username",self.username)
        check_question = self.check_if_exists("questions","id",self.question_id)
        question =self.get_by_key("questions","id",self.question_id)

        self.current_vote = question[0]["votes"]
        if not check_question:
            return jsonify({
                "status": 404,
                "error": "{} not found".format("meetup record")
            }), 404
        else:
            self.user_id = user[0]["id"]
            vote_sql = """ INSERT INTO votes (user_id,question_id,number)
                VALUES('{}','{}','{}') RETURNING votes.id;""".format(self.user_id,self.question_id,self.vote)

            self.save_data(vote_sql)
            vote = self.current_vote +1
            update_sql= """UPDATE questions SET votes='{}'  WHERE id='{}' RETURNING questions.id;""".format(vote,self.question_id)
            self.save_data(update_sql)

            # update question
            question =self.get_by_key("questions","id",self.question_id)
            return jsonify({"status": 201,
                    "vote":question,
                    "message":"sucessfully upvoted question",
            }), 201

    def downvote_question(self,**kwargs):

        self.username=kwargs['username']
        self.question_id=kwargs['question_id']
        self.vote =1

        user = self.get_by_key("users","username",self.username)
        check_question = self.check_if_exists("questions","id",self.question_id)
        question =self.get_by_key("questions","id",self.question_id)

        self.current_vote = question[0]["votes"]
        if not check_question:
            return jsonify({
                "status": 404,
                "error": "{} not found".format("meetup record")
            }), 404
        else:
            self.user_id = user[0]["id"]
            vote_sql = """ INSERT INTO votes (user_id,question_id,number)
                VALUES('{}','{}','{}') RETURNING votes.id;""".format(self.user_id,self.question_id,self.vote)

            self.save_data(vote_sql)
            vote = self.current_vote-1
            update_sql= """UPDATE questions SET votes='{}'  WHERE id='{}' RETURNING questions.id;""".format(vote,self.question_id)
            self.save_data(update_sql)

            # update question
            question =self.get_by_key("questions","id",self.question_id)
            return jsonify({"status": 201,
                    "vote":question,
                    "message":"sucessfully downvoted question",
            }), 201

