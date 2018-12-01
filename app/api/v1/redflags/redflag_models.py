import datetime as dt
from flask import jsonify, make_response, request

redflags = [
    {"id" : 1,
    "createdOn" : "01/04/2018",
   "createdBy" : "juzer",
    "type" : "Red-Flag",
    "location" : "Nairobi",
    "status" : "Under Investigation",
    "image" : "image",
    "video" : "video",
    "title" : "Maize-Scandal",
    "description" : "There has been some..."
    },
    {"id" : 2,
    "createdOn" : "05/12/2018",
    "createdBy" : "oceans",
    "type" : "Red-Flag",
    "location" : "Mombasa",
    "status" : "Draft",
    "image" : "image",
    "video" : "video",
    "title" : "Maize-Scandal",
    "description" : "There has been some..."

    }
]

class RedFlagsModel():

    def __init__(self):
        self.db = redflags

    def save(self, createdBy, location, title):
        data = {
            "id" : len(self.db) + 1,
            "createdOn" : dt.datetime.now(),
            "createdBy" : createdBy,
            "type" : "Red-Flag",
            "location" : location,
            "status" : "Draft",
            "image" : "image",
            "video" : "video",
            "title" : title,
            "description" : "There has been some..."
        }
        
        self.db.append(data)
        
        return self.db

    def get_redflags(self):
        return self.db


