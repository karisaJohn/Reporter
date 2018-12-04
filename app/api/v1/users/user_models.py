import datetime as dt
from flask import jsonify, make_response, request

users = [
    {"id": 1,
    "firstname" : "John",
    "lastname" : "Karisa",
    "othernames" : "Kahindi",
    "email" : "mcu@gmail.com",
    "phoneNumber" : "0718743083",
    "registered" : "01/04/2018",
    "username" : "mcu"
    },
    {"id": 2,
    "firstname" : "Jay",
    "lastname" : "Karis",
    "othernames" : "Kay",
    "email" : "dceu@gmail.com",
    "phoneNumber" : "0712345678",
    "registered" : "01/02/2018",
    "username" : "DCEU"
    }
]


class UsersModel():

    def __init__(self):
        self.db = users

    def save(self, firstname, lastname, othernames, email, phoneNumber, username):
        data = {
            "id" : len(self.db) + 1,
            "firstname" : firstname,
            "lastname" : lastname,
            "othernames" : othernames,
            "email" : email,
            "phoneNumber" : phoneNumber,
            "registered" : dt.datetime.now(),
            "username" : username,
            "isAdmin" : None
        }
        
        self.db.append(data)
        
        return self.db

    def get_users(self):
        return self.db
