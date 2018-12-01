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

    def get_redflag(self, num):
        for redflag in self.db:
            if redflag['id'] == num:
                return redflag

    def edit_redflag(self, num):
        for redflag in self.db:
            if redflag['id'] == num :
                if redflag['status'] == 'Draft':
                    redflag.update(request.get_json())
                    return {
                        'Status' : 200,
                        'data' : [{
                            'id' : num,
                            'message' : 'Upated your changes.'
                        }]
                    }
                
                elif redflag['status'] == 'Under Investigation':
                    return {
                        'status' : 404,
                        'error' : 'Incident under Investigation, cannot make changes.' 
                    }

                elif redflag['status'] == 'Rejected':
                    return {
                        'status' : 404,
                        'error' : 'Incident was Rejected, cannot make changes.' 
                    }

                else :
                    return {
                        'status' : 404,
                        'error' : 'Incident was Resolved, cannot make changes.' 
                    }


