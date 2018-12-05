from flask_restful import Resource
from flask import jsonify, make_response, request
#local import
from .redflag_models import RedFlagsModel

class RedFlags(Resource, RedFlagsModel):
    """docstring for MyFriends"""

    def __init__(self):
        self.db = RedFlagsModel()

    def post(self):
        data_json = request.get_json(force=True)
        if not data_json:
            return {'status' : 200, "Message" : "No input data provided"}
        data = request.get_json()
        createdBy = data['createdBy']
        location = data['location']
        title = data['title']

        self.db.save(createdBy, location, title)
        return make_response(jsonify({
            "Message": "RedFlag added successfully."
            }),201)

    def get(self):
        redflags = self.db.get_redflags()
        if redflags == None:
            return make_response(jsonify({
                "Message" : "No records found."
            }))
        return make_response(jsonify({
                "Records": redflags,
                "Status" : 200
            }),200)


class RedFlag(Resource, RedFlagsModel):
    def __init__(self):
        self.db = RedFlagsModel()

    def get(self, num):
        redflag = self.db.search(num)
        if redflag == None:
            return make_response(jsonify({
                "Error" : "RedFlag does not exit."
            }), 404)
        return make_response(jsonify({
            "Record" : redflag
        }), 200)
    
    def patch(self, num):
        redflag = self.db.search(num)
        if redflag == None:
            return make_response(jsonify({
                "Error" : "RedFlag does not exist."
            }), 404)

        elif redflag["status"] == "Draft":
            self.db.edit_redflag
            return make_response(jsonify({
                "Message" : "Change made successfully."
            }), 200)

        elif redflag["status"] == "Under Investigation":
            return make_response(jsonify({
                "Message" : "RedFlag still under investigation."
            }), 404)

        elif redflag["status"] == "Rejected":
            return make_response(jsonify({
                "Message" : "RedFlag was rejected."
            }), 404)
        
        elif redflag["status"] == "Resolved":
            return make_response(jsonify({
                "Status" : 404,
                "Message" : "RedFlag already resolved."
            }), 404)
    
    def delete(self, num):
        redflag = self.db.search(num)
        if redflag == None:
            return make_response(jsonify({
                "Error" : "RedFlag does not exist."
            }), 404)
        self.db.delete_redflag(redflag)
        return make_response(jsonify({
            "Data" : "Record deleted successfully."
            }), 200)