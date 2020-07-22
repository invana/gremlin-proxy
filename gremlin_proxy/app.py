from flask import Flask
import os
from gremlin_proxy.connector import GremlinHTTPConnectClient
from flask import request

GREMLIN_HOST = os.environ.get("GREMLIN_HOST")
VERSION = os.environ.get("VERSION", "alpha")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


@app.before_request
def authorize_token():
    pass


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route("/", methods=["GET"])
def hello_view():
    return {"message": "Hey there! Happy Gremlin Proxying. Look at https://invana.io/docs",
            "gremlin-hostname": GREMLIN_HOST,
            "version": VERSION}, 200


@app.route("/ping", methods=["GET"])
def pong_view():
    return {"message": "pong"}, 200


gremlin_url = "{}/gremlin".format(GREMLIN_HOST)


def headers_for_gremlin(all_headers):
    interested_header_keys = ["Content-Type", "Authorization"]
    new_data = {}
    for interested_header_key in interested_header_keys:
        new_data[interested_header_key] = all_headers.get(interested_header_key)
    return new_data


@app.route("/gremlin", methods=["POST"])
def gremlin_view():
    headers = headers_for_gremlin(dict(request.headers))
    json_data = request.get_json()
    connector = GremlinHTTPConnectClient(gremlin_url, headers=headers)
    data = connector.execute_raw_query(json_data)
    return data
