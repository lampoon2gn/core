from modules.search import Search
from flask_restful import Resource
import pandas as pd
from flask import request
import csv
import os
from app import app
import boto3, botocore


class Analyze(Resource):
    
    def __init__(self):
        self.ALLOWED_EXTENSIONS = set(['csv'])
    
    def upload_file_to_s3(self, file, bucket_name, acl="public-read"):

        s3 = boto3.client("s3", aws_access_key_id=app.config['S3_KEY'], aws_secret_access_key=app.config['S3_SECRET'])

        try:
            s3.upload_fileobj(
                file,
                bucket_name,
                file.filename,
                ExtraArgs={
                    "ACL": acl,
                    "ContentType": file.content_type
                }
            )
        except Exception as e:
            return repr(e)

        return "{}{}".format(app.config["S3_LOCATION"], file.filename)

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    def get(self):
        return render_template("analyze.html")

    def post(self):

        #s3 = boto3.client("s3", aws_access_key_id=app.config['S3_KEY'], aws_secret_access_key=app.config['S3_SECRET'])
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
            input_file.save(os.path.join('tmp', app.config['UPLOAD_FOLDER'], input_file.filename))
            #output = self.upload_file_to_s3(input_file, app.config["S3_BUCKET"])
            #aws_file = s3.get_object(Bucket=app.config["S3_BUCKET"], Key=input_file.filename)['Body']
            #byte_file = pickle.loads(aws_file.read())
            message = Search.analyze(os.path.join('tmp', app.config['UPLOAD_FOLDER'], input_file.filename)) #Might have to change the CURL filename on request.files['<CURL_FILENAME>']
            os.remove(os.path.join('tmp', app.config['UPLOAD_FOLDER'], input_file.filename))
            return {
                'status_code': 200,
                'input_sheet': input_file.filename,
                'predicted_sheets': message
            }
            return message