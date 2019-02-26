from . import routes, InvalidUsage

@routes.route('/a')
def test():
    raise InvalidUsage('this is error', status_code=500)
    # return 'test'

