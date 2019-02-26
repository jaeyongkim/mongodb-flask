from . import routes, InvalidUsage
from flask import jsonify

@routes.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response