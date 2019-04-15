from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

#APP
app = Flask(__name__)

#API
api = Api(app)
base_path = '/api/v1'

import resources
###############################################################################################

api.add_resource(resources.AllSheets, '{}/all'.format(base_path))
api.add_resource(resources.Analyze, '{}/analyze'.format(base_path))