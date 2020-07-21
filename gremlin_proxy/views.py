"""
Views of gremlin connector with http.
"""
from flask_restful import Resource
from connector import GremlinHTTPConnectClient
from gremlin_proxy.auth import InvanaTokenAuth
from flask import request
import os

GREMLIN_HOST = os.environ.get("GREMLIN_HOST")

if GREMLIN_HOST is None:
    raise Exception("InvalidAPIURL. Use something like http://127.0.0.1:8182 as gremlin host")


class GremlinQueryView(Resource):
    """

    """

    @staticmethod
    def get_connector():
        # return GremlinWSConnectorClient(API_URL)
        gremlin_url = "{}/gremlin".format(GREMLIN_HOST)
        return GremlinHTTPConnectClient(gremlin_url)

    def post(self):
        token = request.headers.get('Authorization')
        json_data = request.get_json()
        gremlin_query = json_data.get("gremlin")
        auth = InvanaTokenAuth(auth_data=token)
        is_valid = auth.check_is_validate()
        if not is_valid:
            raise Exception("Invalid Authentication. Please refer docs")
        connector = self.get_connector()
        return connector.execute_raw_query(gremlin_query)
