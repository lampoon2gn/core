from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

#APP
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = $(heroku config:get DATABASE_URL -a saudagar-core)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yukalangbuana:yukalangbuana@localhost:5432/asiamajor' #====> LOCAL DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#API
api = Api(app)
base_path = '/api/v1'

#DATABASE
db = SQLAlchemy(app)

#CORS
CORS(app)

import resources, models
###############################################################################################

api.add_resource(resources.Analyze, '{}/analyze'.format(base_path))