from . import routes
from ..controllers.login import *

@routes.route('/')
def index():
    return 'hi'


@routes.route('/user/get')
def user():
    print(get_user())
    return 'get'


@routes.route('/user/save')
def user_make():
    create_new_member()
    print(get_user())
    return 'save'