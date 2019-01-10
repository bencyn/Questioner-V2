from flask import Flask, json, jsonify, request, make_response, Blueprint
from datetime import datetime

from ..models.questions_model import Question
from app.v1 import v1

question_object=Question()

@v1.route("/meetups/<int:meetup_id>/questions", methods=['POST'])
def create_question(meetup_id):
    """ post method that creates a question posted in a specific meeting """
    try:
        title = request.get_json()['title']
        body = request.get_json()['body']

    except KeyError:
        return jsonify({'status': 400,
                        ' error': "question data required"})

    if not title:
        return validate_input("title")
    
    if not body:
        return validate_input("body")
    else:
        question_object.add_question(1,meetup_id,title,body)

        return jsonify({"status": 201,
                        "data":[{"title": title,
                                "user_id":len(question_object)+1,
                                "meetup": meetup_id,
                                "body": body}]}), 201

@v1.route("/questions/<int:question_id>/upvote", methods=['PATCH'])
def upvote_question(question_id):
    """ question upvote endpoint logic"""

    question = question_object.get_question(question_id)
    if question:
        upvote_question = question[question_id]
        upvote_question['votes'] = upvote_question['votes'] + 1
        return jsonify({"status": 200, "data": upvote_question}), 200
    return jsonify({"status": 404, "error": "Question not found"}), 404


@v1.route("/questions/<int:question_id>/downvote", methods=['PATCH'])
def downvote_question(question_id):
    """ question downvote endpoint logic """
   
    question = question_object.get_question(question_id)
    if question:
        downvote_question = question[question_id]
        downvote_question['votes'] = downvote_question['votes'] - 1
        return jsonify({"status": 200, "data": downvote_question}), 200
    return jsonify({"status": 404, "error": "Question not found"}), 404


def validate_input(field):
     return make_response(jsonify({
            "status": 400,
            "message": "{} cannot be empty".format(field)
        })), 400