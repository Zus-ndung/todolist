from flask import request, Blueprint

todoRoute = Blueprint("todo", __name__)


@todoRoute.route("/getall", methods=['GET'])
def getAll():
    return "abc"
