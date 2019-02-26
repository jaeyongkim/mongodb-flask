from flask import Blueprint
from ..controllers.error_handle import InvalidUsage

routes = Blueprint('routes', 'routes')

from .user import *
from .test import *
from .error import *
