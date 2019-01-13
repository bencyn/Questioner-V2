from flask import json, jsonify , make_response


class Validators():

    def __init__(self):
        pass

    def validate_input(self,field):
        return make_response(jsonify({
                "status": 400,
                "message": "{} cannot be empty".format(field)
            })), 400