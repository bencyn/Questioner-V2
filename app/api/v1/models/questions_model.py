from datetime import datetime

questions=[]

class Question(object):
    """ questions class """
    pass

    def __init__(self):
        """initialize and define objects"""
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

    def get_question(self,id):
        ''' get question by key id '''
        for question in questions:
            if question["id"]==id:
                return question