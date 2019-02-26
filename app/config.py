# coding: utf-8

class Config(object):
    section_name = None
    def __init__(self):
        if not self.section_name:
            return

class DevelopmentConfig(Config):
    section_name = 'development'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_DATABASE = 'flask_mongo_test'
    pass

class ProductionConfig(Config):
    section_name = 'production'
    pass


def init_app(app, config_name):
    app.config.from_object({
                           'development': DevelopmentConfig,
                           'production': ProductionConfig,
    }[config_name]())
