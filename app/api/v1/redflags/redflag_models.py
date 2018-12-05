import datetime as dt
from flask import jsonify, make_response, request

redflags = []

class RedFlagsModel():

    def __init__(self):
        self.db = redflags

    def search(self, num):
        "method for searching a redflag in a list."
        for redflag in self.db:
            if redflag["id"] == num:
                return redflag
        return None

    def redflagid(self):
        if len(self.db):
            return self.db[-1]["id"] + 1
        return 1

    def save(self, createdBy, location, title):
        data = {
            "id" : self.redflagid(),
            "createdOn" : "today",
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
        if len(self.db) == 0:
            return None
        return self.db

    def edit_redflag(self, redflag):
        redflag.update(request.get_json())

    def delete_redflag(self, redflag):
        self.db.remove(redflag)
