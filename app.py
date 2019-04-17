from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

#CONFIG
UPLOAD_FOLDER = 'UPLOADS/'
ALLOWED_EXTENSIONS = set(['csv'])

#APP
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yukalangbuana:yukalangbuana@localhost/asiamajor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#API
api = Api(app)
base_path = '/api/v1'

#DATABASE
db = SQLAlchemy(app)

import resources, models
###############################################################################################

api.add_resource(resources.AllSheets, '{}/all'.format(base_path))
api.add_resource(resources.Analyze, '{}/analyze'.format(base_path))