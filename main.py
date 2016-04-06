from flask import Flask
import os
from flask_restful import Resource, Api
from flask_restful import reqparse
import requests

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

class Hello(Resource):
	def get(self):
		parser = reqparse.RequestParser()
		parser.add_argument('token', type=str, required=True, help='Please provide your LIFX Token')
		args = parser.parse_args()
		token = args['token']
		headers = {
		    "Authorization": "Bearer %s" % token,
		}
		# response = requests.get('https://api.lifx.com/v1/lights/all', auth=(token, ''))

		# trigger change
		return {'token': token, 'response status': 'test'}
		

api.add_resource(Hello, '/token')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)