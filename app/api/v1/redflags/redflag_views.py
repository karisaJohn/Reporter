from flask_restful import Resource
from flask import jsonify, make_response, request
#local import
from .redflag_models import RedFlagsModel

class RedFlags(Resource, RedFlagsModel):
    """docstring for MyFriends"""

    def __init__(self):
        self.db = RedFlagsModel()

    def post(self):
        data = request.get_json()
        createdBy = data['createdBy']
        location = data['location']
        title = data['title']

        resp = self.db.save(createdBy, location, title)
        return make_response(jsonify({"Users":resp}),201)

    def get(self):
        resp = self.db.get_redflags()
        return make_response(jsonify(
            {
                "Users":resp,
                "status" : 200
            }),200)


class RedFlag(Resource, RedFlagsModel):
    def __init__(self):
        self.db = RedFlagsModel()

    def get(self, num):
        resp = self.db.get_redflag(num)
        return make_response(jsonify({"Users":resp}),200)


