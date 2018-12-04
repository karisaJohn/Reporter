
from flask_restful import Resource
from flask import jsonify, make_response, request
#local import
from .user_models import UsersModel


class Users(Resource, UsersModel):
    def __init__(self):
        self.db = UsersModel()
        
    def post(self):
        data = request.get_json()
        firstname = data['firstname']
        lastname = data['lastname']
        othernames = data['othernames']
        email = data['email']
        phoneNumber = data['phoneNumber']
        username = data['username']        

        resp = self.db.save(firstname, lastname, othernames, email, phoneNumber, username)
        return make_response(jsonify({"Users":resp}),201)

    def get(self):
        resp = self.db.get_users()
        return make_response(jsonify({"Users":resp}),200)       