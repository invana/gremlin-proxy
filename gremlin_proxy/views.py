"""
Views of gremlin connector with http.
"""
from flask_restful import Resource

import os

GREMLIN_HOST = os.environ.get("GREMLIN_HOST")

if None in [GREMLIN_HOST]:
    raise Exception("""
Invalid GREMLIN_HOST.   
    
Example:
GREMLIN_HOST Eg: http://127.0.0.1:8182
    """)


class GremlinQueryView(Resource):
    """

    """

