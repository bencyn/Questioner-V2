from datetime import datetime

questions=[]

class Question(object):
    """ questions class """
    pass

    def __init__(self):
        self.question = question

# {
# “id” : Integer,
# “createdOn” : Date,
# “createdBy” : Integer, // represents the user asking the question
# “meetup” : Integer, // represents the meetup the question is for
# “title” : String,
# “body” : String,
# “votes” : Integer,
# ...
# }
    def add_question(self,createdBy,meetup,title,body,votes):
        """" defines the logic for adding a question """

        createdOn = datetime.now()

        question = {
            "id": len(self.question) + 1,
            "createdOn":createdOn,
            "createdBy":createdBy,
            "meetup":meetup,
            "title":title,
            "body":body,
            "votes":2
        }
        self.question.apppend(question)
        return question