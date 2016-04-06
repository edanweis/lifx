from flask import Flask
import os
from flask_restful import Resource, Api
from flask_restful import reqparse
import requests

app = Flask(__name__)
api = Api(app)

class Help(Resource):
    def get(self):
        return "Try pointing your browser to lifx.herokuapp.com/?token=your_LIFX_API_token_goes_here"

api.add_resource(Help, '/help')

class Base(Resource):
	def get(self):
		parser = reqparse.RequestParser()
		parser.add_argument('token', type=str, required=True, help='Please provide your LIFX Token')
		args = parser.parse_args()
		token = args['token']
		headers = {"Authorization": "Bearer %s" % token}
		response = requests.get('https://api.lifx.com/v1/lights/all', headers=headers)

		
		return {'token' : token, 'response' : response.json(), 'status' : self.getResponseCode(response.status_code)}
		

	def getResponseCode(self, code):
		responses ={200 : "OK - Everything worked as expected", 201 : "Created - One light has accepted the request. Will be replaced by 202 in next version.", 207 : "Multi-Status - Many lights have accepted the request. Inspect the response body for individual statuses. Will be replaced by 202 and 408 in next version.", 401 : "Unauthorized - Bad access token.", 404 : "Not Found - Selector is malformed or did not match any lights.", 408 : "Request Timeout - One light may be physically powered off or unreachable.", 422 : "Unprocessable Entity - Missing or malformed parameters.", 426 : "Upgrade Required - HTTP was used to make the request instead of HTTPS. Repeat the request using HTTPS instead.", 429 : "Too Many Requests - request exceeded a rate limit. See the Rate Limits section.", 500 : "Server Error", 502 : "Server Error", 503 : "Server Error", 523 : "Server Error"}
		return responses[code]

api.add_resource(Base, '/')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)