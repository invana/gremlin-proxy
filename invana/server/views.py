"""
Views of gremlin connector with http.
"""
from flask_restful import Resource
from graph.connector import GremlinHTTPConnectClient, GremlinWSConnectorClient
from server.auth import InvanaTokenAuth
from flask import request


class GremlinQueryView(Resource):
    """

    """

    @staticmethod
    def get_connector(protocol):
        if protocol == "ws":
            return GremlinWSConnectorClient("ws://192.168.0.10:8182/gremlin")
        else:
            return GremlinHTTPConnectClient("http://192.168.0.10:8182/gremlin")

    def post(self):
        protocol = request.args.get('protocol')

        token = request.headers.get('Authorization')
        json_data = request.get_json()
        gremlin_query = json_data.get("gremlin")
        auth = InvanaTokenAuth(auth_data=token)
        is_valid = auth.check_is_validate()
        if not is_valid:
            raise Exception("Invalid Authentication. Please refer docs")
        connector = self.get_connector(protocol)
        return connector.execute_raw_query(gremlin_query)


