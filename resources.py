from flask_restful import Resource

class AllSheets(Resource):
    def get(self):
        return {
            'status_code': 200,
            'message': "API end-point to list all the sheets"
        }

class Analyze(Resource):
    def post(self):
        return {
            'status_code': 200,
            'message': 'API end-point for uploading a sheet for analysis'
        }