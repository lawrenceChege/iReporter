""" This module does validation for data input in incidents """
import re
from flask import request

class Validate():
    """
        methods for validatin incidents input data
    """
    
    def __init__(self):
        self.args = request.get_json()
        self.title = self.args["title"]
        self.description = self.args["description"]
        self.type = self.args["type"]

    def check_redflag(self):
        self.check_title()
        self.check_description()
        self.check_type()

    def check_email(self):
        pass

    def check_password(self):
        pass
    
    def check_username(self):
        pass

    def check_title(self):
        if isinstance(self.args["title"], str) and len(self.title) == 0:
            return {"message": "Title string is required "}
        return None

    def check_description(self):
        if isinstance(self.args["description"], str) and len(self.description) == 0:
            return {"message": "Description string is required "}
        return None


    def check_type(self):
        if isinstance(self.args["type"], str) and len(self.type) == 0:
            return {"message": "Type string is required "}
        return None


    