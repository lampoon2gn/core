from modules.search import Search
from flask_restful import Resource
import pandas as pd
from flask import request
import csv
import os
from app import app

class AllSheets(Resource):
    def get(self):
        return {
            'status_code': 200,
            'message': "API endpoint for getting all the sheets"
        }


class Analyze(Resource):
    
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def post(self):
        input_file = request.files['']
        input_file.save(os.path.join(app.config['UPLOAD_FOLDER'], input_file.filename))
        message = Search.analyze(os.path.join(app.config['UPLOAD_FOLDER'], input_file.filename)) #Might have to change the CURL filename on request.files['<CURL_FILENAME>']
        return {
            'status_code': 200,
            'sheets': message
        }