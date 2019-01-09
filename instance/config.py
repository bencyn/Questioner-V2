import os
'''configuration options'''

class Config(object):
    '''Parent configuration class'''
    DEBUG = False
    SECRET_KEY = 'tryandguess'
    ENV = 'development'
    SECRET = os.getenv('SECRET')


class DevelopmentConfig(Config):
    '''configurations for development environment'''
    DEBUG = True

class TestingConfig(Config):
    '''configurations for test environment'''
    DEBUG = True


class ProductionConfig(Config):
    '''configurations for production environment'''
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
