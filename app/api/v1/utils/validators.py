from flask import json, jsonify , make_response


class Validators():
    """ global validation methods """
    def __init__(self):
        pass

    def validate_input(self,field):
        """ validates empty input"""
        return make_response(jsonify({
                "status": 400,
                "error": "{} cannot be empty".format(field)
            })), 400
    
    def validate_missing_data(self):
        """ validates missing json object"""
        return jsonify({'status': 400,
                        ' error': "Bad request: attach missing fields"}),400