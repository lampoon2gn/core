from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os

#APP
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jbdspjaddeofzc:8f2c92ef9ac427ef0274417ccc235e6d420fe4ff57be9f009b89ddb4f06dedd5@ec2-54-225-113-7.compute-1.amazonaws.com:5432/d1v6cjh3kibd5f' #HEROKU DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#API
api = Api(app)
base_path = '/api'

#DATABASE
db = SQLAlchemy(app)

#CORS
CORS(app)

import resources, models
###############################################################################################

api.add_resource(resources.Ping, '{}/ping'.format(base_path))
api.add_resource(resources.Analyze, '{}/analyze'.format(base_path))