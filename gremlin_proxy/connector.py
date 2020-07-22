import urllib.parse
import urllib.request
import json


class GremlinHTTPConnectClient:

    def __init__(self, gremlin_server_url, headers=None):
        if headers is None:
            headers = {}
        if gremlin_server_url is None:
            raise Exception("Invalid gremlin_server_url. default: ws://127.0.0.1:8182/gremlin")
        self.gremlin_server_url = gremlin_server_url
        self.headers = headers

    def execute_raw_query(self, query_json):
        """
        :param query_json: eg:  {'gremlin': 'g.V().limit(5).toList()'}
        :return:
        """
        params = json.dumps(query_json).encode('utf8')
        req = urllib.request.Request(self.gremlin_server_url, params, self.headers)
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read())

    def close(self):
        pass
