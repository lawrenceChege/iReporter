"""
This module runs the app and tests 
"""
import os
from app import create_app
from migrations import create_tables
config = os.getenv('FLASK_CONFIG')

# APP = create_app(config)
APP = create_app("development")
create_tables('main')
create_tables('test')
if __name__ == "__main__":
    APP.run(debug = True)