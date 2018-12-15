"""
    This module sets up the configurations for running the app
"""
import os


class Config:
    """
        This defines the base config class
    """

    DEBUG = False
    BUNDLE_ERRORS = True
    JWT_SECRET_KEY = '234tghn !#ED'
    JWT_ACCESS_TOKEN_EXPIRES = os.getenv('JWT_ACCESS_TOKEN_EXPIRES')
    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    ACCOUNT_SID = 'AC5fb68dc450455c042753a812998a0d21'
    AUTH_TOKEN = '255b0433548f74e4e9e952543c6eb331'
    ADMIN_PHONE = '+16786162418'

class HerokuConfig(Config):
    """
        Thsi defines the development environment of the app
    """
    PROPAGATE_EXEPTIONS = True
    DEBUG = True
    DATABASE = os.getenv('DATABASE_URL')
    DB_NAME = os.getenv('DB_NAME')
    DATABASE_URL = 'postgres://gqpylxymapzcup:ebd641e7c5bd2116a79f179a869557f684818b0df68a0379a528330987886192@ec2-184-72-239-186.compute-1.amazonaws.com:5432/d2hukbh74b0mkk'
class DevelopmentConfig(Config):
    """
        Thsi defines the development environment of the app
    """
    PROPAGATE_EXEPTIONS = True
    DEBUG = True
    DATABASE = os.getenv('DATABASE_URL')
    DB_NAME = os.getenv('DB_NAME')
    DATABASE_URL = 'postgresql://localhost/ireporter?user=postgres&password=12345678'


class TestingConfig(Config):
    """
        This defines the testing environment for the app
    """
    TESTING = True
    DEBUG = True
    DATABASE = os.getenv('DATABASE_URL')
    DB_NAME = os.getenv('TEST_DB_NAME')
    DATABASE_URL = 'postgresql://localhost/test?user=postgres&password=12345678'



class ProductionConfig(Config):
    """
        This defines the production environment fro the app
    """
    DEBUG = False
    TESTING = False
    DB_NAME = os.getenv('DB_NAME')
    DATABASE_URL = os.getenv('DATABASE_URL')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': HerokuConfig
}
