from flask import Blueprint
from flask-restplus import Api

version_one = Blueprint("v1", __name__, url_prefix="ireporter/api/v1")

