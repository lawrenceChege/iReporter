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
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = os.getenv('JWT_ACCESS_TOKEN_EXPIRES')
    # Database
    DB_HOST = os.getenv('DB_HOST')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    # User
    ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')


class DevelopmentConfig(Config):
    """
        Thsi defines the development environment of the app
    """
    PROPAGATE_EXEPTIONS = True
    DEBUG = True    
    DB_NAME = os.getenv('DB_NAME')
    DATABASE_URL = os.getenv('DATABASE_URL')


class TestingConfig(Config):
    """
        This defines the testing environment for the app
    """
    TESTING = True
    DEBUG = True
    TEST_DATABASE_URL = os.getenv('TEST_DATABASE_URL')    
    DB_NAME = os.getenv('DB_TEST_NAME')


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
    'default': DevelopmentConfig
}
