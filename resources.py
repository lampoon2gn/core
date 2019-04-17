from modules.search import Search
from flask_restful import Resource
import pandas as pd
from flask import request
import os
from app import app


class Analyze(Resource):
    
    def __init__(self):
        self.ALLOWED_EXTENSIONS = set(['csv'])

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    def get(self):
        return render_template("analyze.html")

    def post(self):

        if request.files['file'].filename == '':
            return {
                'status_code': 400,
                'message': 'Invalid request: No file detected.'
            }
        
        input_file = request.files['file']
        if not self.allowed_file(input_file.filename):
            return {
                'status_code': 422,
                'message': 'File extension is not allowed'
            }
        else:
            input_file.save(os.path.join('/tmp/', input_file.filename))
            message = Search.analyze(os.path.join('/tmp/', input_file.filename)) #Might have to change the CURL filename on request.files['<CURL_FILENAME>']
            os.remove(os.path.join('/tmp/', input_file.filename))
            return {
                'status_code': 200,
                'input_sheet': input_file.filename,
                'predicted_sheets': message
            }
            return message