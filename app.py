from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

#APP
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://epbwbeeuzkuhwa:a5c4009f63a95fa6266d17e27dc5b600dd716dbed12b7585cbdcb28961fcb0dc@ec2-54-225-113-7.compute-1.amazonaws.com:5432/d1v6cjh3kibd5f'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yukalangbuana:yukalangbuana@localhost:5432/asiamajor' #====> LOCAL DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#API
api = Api(app)
base_path = '/api/v1'

#DATABASE
db = SQLAlchemy(app)

import resources, models
###############################################################################################

api.add_resource(resources.Analyze, '{}/analyze'.format(base_path))