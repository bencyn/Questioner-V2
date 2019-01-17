from flask import Flask, json, jsonify, request, make_response, Blueprint
from datetime import datetime
import app
from ..models import questions_model
from ....api.v2 import v2

question_object=questions_model.Question()

@v2.route("/meetups/<int:meetup_id>/questions", methods=['POST'])
@app.jwt_required
def create_question(meetup_id):
    """ post method that creates a question posted in a specific meeting """

    data = request.get_json()

    if not data:
        return jsonify({"Message": 'Cannot send empty data'}),409
    else:
        title = request.get_json()['title']
        body = request.get_json()['body']
        
        
        val_input = {"title":title,"body":body}

        for key,value in val_input.items():
            if not value.strip():
                return make_response(jsonify({
                    "status": 400,
                    "error": "{} cannot be empty".format(key)
                })), 400

        question_object.add_question(meetup_id,title,body)

        return jsonify({"status": 201,
                        "data":[{"title": title,
                                "user_id":len(question_object.questions)+1,
                                "meetup": meetup_id,
                                "body": body}]}), 201

@v2.route("/questions/<int:question_id>/upvote", methods=['PATCH'])
@app.jwt_required
def upvote_question(question_id):
    """ question upvote endpoint logic """

    question = question_object.get_question(question_id)
    
    if question:
        upvote_question = question
        upvote_question['votes'] = upvote_question['votes'] + 1
        return jsonify({"status": 200, "data": upvote_question}), 200

    return jsonify({"status": 404, "error": "Question not found"}), 404


@v2.route("/questions/<int:question_id>/downvote", methods=['PATCH'])
@app.jwt_required
def downvote_question(question_id):
    """ question downvote endpoint logic """
   
    question = question_object.get_question(question_id)
    
    if question:
        downvote_question = question
        downvote_question['votes'] = downvote_question['votes'] - 1
        return jsonify({"status": 200, "data": downvote_question}), 200


    return jsonify({"status": 404, "error": "Question not found"}), 404

