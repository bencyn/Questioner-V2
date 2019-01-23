import os
'''configuration options'''

class Config(object):
    '''Parent configuration class'''
    
    SECRET = os.getenv('SECRET')
    DATABASE_URL = os.getenv("DATABASE_URL")
    DEBUG = True
    TESTING = False

    
class DevelopmentConfig(Config):
    '''configurations for development environment'''
    DEBUG = True

class TestingConfig(Config):
    '''configurations for test environment'''
    TESTING = True
    DEBUG=True
    DATABASE_URL = os.getenv("TEST_DATABASE_URL")

class ProductionConfig(Config):
    '''configurations for production environment'''
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
