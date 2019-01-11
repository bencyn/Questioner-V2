from datetime import datetime

questions=[]

class Question(object):
    """ questions class """
    pass

    def __init__(self):
        self.questions = questions

    def add_question(self,meetup,title,body,votes=0):
        """" defines the logic for adding a question """

        createdOn = datetime.now()

        question = {
            "id": len(self.questions) + 1,
            "createdOn":createdOn,
            "createdBy":len(self.questions)+1,
            "meetup":meetup,
            "title":title,
            "body":body,
            "votes":2
        }
        self.questions.append(question)
        return question

    
    # def get_meetups(self):
    #     return self.meetups

    def get_question(self,id):
        return self.questions[id]