from flask_restful import Api, Resource
from flask import Blueprint

#local imports
from .redflags.redflag_views import RedFlags, RedFlag
from .users.user_views import Users

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)

api.add_resource(RedFlags, '/redflags')
api.add_resource(Users, '/users')
api.add_resource(RedFlag, '/redflags/<int:num>')
