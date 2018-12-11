"""
This module runs the app and tests
"""
import os
from app import create_app
from migrations import DbModel
config = os.getenv('FLASK_CONFIG')

db=DbModel('main')
testdb = DbModel('test')
APP = create_app("development")
db.create_tables()
testdb.create_tables()

if __name__ == "__main__":
    APP.run(debug = True)