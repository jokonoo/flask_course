from flask_restx import Namespace, Resource

api = Namespace('movies', description='Movies related operations')


@api.route("/test")
class Test(Resource):
    def get(self):
        return {"test": "test"}
