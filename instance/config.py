import os
'''configuration options'''

class Config(object):
    '''Parent configuration class'''
    
    DEBUG = False
    ENV = 'development'
    SECRET = os.getenv('SECRET')
    DATABASE_URL =os.getenv('DATABASE_URL')
    TEST_DATABASE_URL =os.getenv('TEST_DATABASE_URL')


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
