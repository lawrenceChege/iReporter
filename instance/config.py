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
    # JWT_ACCESS_TOKEN_EXPIRES = os.getenv('JWT_ACCESS_TOKEN_EXPIRES')


class DevelopmentConfig(Config):
    """
        Thsi defines the development environment of the app
    """
    
    DEBUG = True


class TestingConfig(Config):
    """
        This defines the testing environment for the app
    """
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    """
        This defines the production environment fro the app
    """
    DEBUG = False
    TESTING = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
