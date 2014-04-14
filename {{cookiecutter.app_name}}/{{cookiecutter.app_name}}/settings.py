import os

class Config(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    DATABASE_URI = 'sqlite://%s' % os.path.join(APP_DIR, 'test.db')
    DEBUG = True

class ProdConfig(Config):
    '''Production configuration.'''
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = False

class DevConfig(Config):
    '''Development configuration.'''
    SECRET_KEY = 'devsecretkey'

class TestingConfig(Config):
    SECRET_KEY = 'testsecretkey'
    DATABASE_URI = 'sqlite://:memory:'
