from flask import Blueprint, jsonify
from flask_jwt_extended import JWTManager



errors = Blueprint('errors', __name__)

@errors.app_errorhandler(401)
def Unauthorised(e):
    return jsonify ({"status": 401,
        "error": "You do not have permission to access this resource"})

@errors.app_errorhandler(500)
def serverError(e):
    return jsonify({"status": 500,
        "error": "Oops! something went wrong!"})

@errors.app_errorhandler(404)
def not_found(e):
    return jsonify({"status": 404,
        "error": "Resource Not found !"})

@errors.app_errorhandler(405)
def not_allowed(e):
    return jsonify({"status": 405,
        "error": "Method Not allowed on this route!"})
