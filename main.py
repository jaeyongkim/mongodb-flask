# -*- coding: utf-8; -*-
from flask import Flask
from app import config
from app.api.views import *
from app.api.models import db
from wsgiref.simple_server import make_server


def flask_init_app(mode='development'):
    app = Flask('base_app')
    app.register_blueprint(routes)
    config.init_app(app, mode)
    db.init_app(app)
    return app

if __name__ == '__main__':
    demo_server = make_server('127.0.0.1', 5000, flask_init_app())
    demo_server.serve_forever()
    # app = flask_init_app()
    # app.run()
