from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection as _DriverRemoteConnection
from gremlin_proxy.serializers import GremlinResponseSerializer
from gremlin_python.driver import client
import urllib.parse
import urllib.request
import json


class DriverRemoteConnection(_DriverRemoteConnection):

    def submit(self, bytecode):
        result_set = self._client.submit(bytecode)
        results = result_set.all().result()
        return self.response_serializer.serializer_data(results)


class GremlinHTTPConnectClient:
    response_serializer = GremlinResponseSerializer()

    def __init__(self, gremlin_server_url, headers=None):
        if headers is None:
            headers = {'content-type': 'application/json'}
        if gremlin_server_url is None:
            raise Exception("Invalid gremlin_server_url. default: ws://127.0.0.1:8182/gremlin")
        self.gremlin_server_url = gremlin_server_url
        self.headers = headers

    def execute_raw_query(self, raw_query):
        """
        :param raw_query: Gremlin query in plain string.
        :return:
        """

        json_query = {'gremlin': raw_query}
        params = json.dumps(json_query).encode('utf8')
        # TODO - look for connection caching mechanism
        req = urllib.request.Request(self.gremlin_server_url, params, self.headers)
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read())

    def close(self):
        pass


class GremlinWSConnectorClient:
    """
    client = GraphClient("ws://127.0.0.1:8182/gremlin")
    client.
    """

    response_serializer = GremlinResponseSerializer()

    def __init__(self, gremlin_server_url, headers=None):
        if headers is None:
            headers = {}
        if gremlin_server_url is None:
            # TODO - websockets are expensive.
            raise Exception("Invalid gremlin_server_url. default: ws://127.0.0.1:8182/gremlin")
        self.client = client.Client(gremlin_server_url, 'g')

    def execute_raw_query(self, raw_query):
        """
        :param raw_query: Gremlin query in plain string.
        :return:
        """
        result_set = self.client.submit(raw_query)
        future_results = result_set.all()
        data = future_results.result()
        self.close()
        return data

    def close(self):
        self.client.close()
