from flask import Flask, json, jsonify, request, make_response, Blueprint
from datetime import datetime

from ..models import questions_model
from app.api.v1 import v1

question_object=questions_model.Question()

@v1.route("/meetups/<int:meetup_id>/questions", methods=['POST'])
def create_question(meetup_id):
    """ post method that creates a question posted in a specific meeting """
   
    try:
        title = request.get_json()['title']
        body = request.get_json()['body']

    except KeyError:
        return jsonify({'status': 400,
                        ' error': "question data required"})

    question_object.add_question(meetup_id,title,body)

    return jsonify({"status": 201,
                    "data":[{"title": title,
                            "user_id":len(question_object.questions)+1,
                            "meetup": meetup_id,
                            "body": body}]}), 201

@v1.route("/questions/<int:question_id>/upvote", methods=['PATCH'])
def upvote_question(question_id):
    """ question upvote endpoint logic"""

    question = question_object.get_question(question_id)
    
    if question:
        upvote_question = question
        upvote_question['votes'] = upvote_question['votes'] + 1
        return jsonify({"status": 200, "data": upvote_question}), 200

    return jsonify({"status": 404, "error": "Question not found"}), 404


@v1.route("/questions/<int:question_id>/downvote", methods=['PATCH'])
def downvote_question(question_id):
    """ question downvote endpoint logic """
   
    question = question_object.get_question(question_id)
    
    if question:
        downvote_question = question
        downvote_question['votes'] = downvote_question['votes'] - 1
        return jsonify({"status": 200, "data": downvote_question}), 200


    return jsonify({"status": 404, "error": "Question not found"}), 404

