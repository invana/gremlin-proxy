from flask import Flask
from flask_restful import Api
from gremlin_proxy.views import GremlinQueryView
from flask_restful import Resource
from flask_cors import CORS
import os
from connector import GremlinHTTPConnectClient
from flask import request

GREMLIN_HOST = os.environ.get("GREMLIN_HOST")
VERSION = os.environ.get("VERSION", "alpha")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
api = Api(app)
cors = CORS(app, supports_credentials=True )


@app.before_request
def authorize_token():
    pass


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


class HomeView(Resource):
    """

    """

    def get(self):
        return {"message": "Hey there! Happy connecting the Dots with InvanaGraph.",
                "hostname": GREMLIN_HOST,
                "version": VERSION}, 200


class PingPongView(Resource):
    """

    """

    def get(self):
        return {"message": "pong"}, 200


api.add_resource(HomeView, '/')
api.add_resource(PingPongView, '/ping')
# api.add_resource(GremlinQueryView, '/gremlin')
gremlin_url = "{}/gremlin".format(GREMLIN_HOST)


def headers_for_gremlin(all_headers):
    interested_header_keys = ["Content-Type", "Authorization"]
    new_data = {}
    for interested_header_key in interested_header_keys:
        new_data[interested_header_key] = all_headers.get(interested_header_key)
    return new_data


@app.route("/gremlin", methods=["POST"])
def post():
    headers = headers_for_gremlin(dict(request.headers))
    json_data = request.get_json()
    connector = GremlinHTTPConnectClient(gremlin_url, headers=headers)
    data = connector.execute_raw_query(json_data)
    return data


if __name__ == '__main__':
    app.run(debug=True)
