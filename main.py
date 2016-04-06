from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
import requests

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello():
    return "Hello World!"

# class Hello(Resource):
# 	def get(self):
# 		parser = reqparse.RequestParser()
# 		parser.add_argument('location', type=str, required=False)
# 		args = parser.parse_args()
# 		# auth_payload = {"uid": args['location']}
# 		token = args['token']
# 		headers = {
# 		    "Authorization": "Bearer %s" % token,
# 		}
# 		response = requests.get('https://api.lifx.com/v1/lights/all', auth=(token, ''))
# 		# trigger change
# 		return response.status

# api.add_resource(Hello, '/')

if __name__ == '__main__':
	app.run(port=33507, debug=True)