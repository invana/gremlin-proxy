from flask import Flask
from flask_restful import Api
from server.views import GremlinView
from flask_restful import Resource
from flask_cors import CORS

import os

HOST_NAME = os.environ.get("HOST_NAME", "localhost")
VERSION = os.environ.get("VERSION", "alpha")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


class HomeView(Resource):
    """

    """

    def get(self):
        return {"message": "Hey there! Happy connecting the Dots with InvanaGraph.",
                "hostname": HOST_NAME,
                "version": VERSION}, 200


class PingPongView(Resource):
    """

    """

    def get(self):
        return {"message": "pong"}, 200


api.add_resource(HomeView, '/')
api.add_resource(PingPongView, '/ping')
api.add_resource(GremlinView, '/gremlin')

if __name__ == '__main__':
    app.run(debug=True)
