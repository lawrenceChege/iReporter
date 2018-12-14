"""
This module runs the app and tests
"""
import os
from app import create_app
from migrations import DbModel
from werkzeug.exceptions import NotFound
config = os.getenv('FLASK_CONFIG')


APP = create_app("default")
with APP.app_context():
        db = DbModel()
        db.init_db(APP)
        db.create_tables()
@APP.errorhandler(NotFound)
def handle_Bad_Request(error): 
        '''Return a custom message and 404 status code'''
        return {'ststus':404, 'error': 'There is nothing here'}, 404

if __name__ == "__main__":
    APP.run(debug = True)
