"""
This module runs the app and tests 
"""
import os
import click
import subprocess

from app import create_app

APP = create_app(os.getenv('FLASK_CONFIG'))

# @app.cli.command()
# @click.argument('path', default=os.path.join('app'. 'tests'))
# def test(path):
#     """
#         This fuction runs tests with pytest. 
#         It takes the test path as the parameter and
#         returns the subprocees call for tests as the result
#     """

#     cmd = 'py.test -v {0}'.format(path)
#     return subprocess.call(cmd, shell = True)


# @app.cli.command()
# @click.argument('path', default='app')
# def coverage(path):
#     """
#         This fuction generates a coverage report for the tests.
#         It takes the test path as the parameter and
#         returns the subprocess call for coverage as the result
#     """

#     cmd = 'py.test -v --cov-report term-missing --cov {0}'.format(path)
#     return subprocess.call(cmd, shell = True)


if __name__ == "__main__":
    APP.run(debug = True)