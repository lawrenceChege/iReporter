"""
This module runs the app and tests 
"""
import os
from app import create_app
from migrations import DbModel
config = os.getenv('FLASK_CONFIG')


APP = create_app("development")

if __name__ == "__main__":
    APP.run(debug = True)