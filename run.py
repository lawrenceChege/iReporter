"""
This module runs the app and tests 
"""
import os
from app import create_app
# APP = create_app(os.getenv('FLASK_CONFIG'))
APP = create_app("DEVELOPMENT")
if __name__ == "__main__":
    APP.run(debug = True)