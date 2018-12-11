""" This module does validation for data input in incidents """
import re

class Validate():
    """
        methods for validatin incidents input data
    """

    def valid_email(self, email):
        vemail = re.match(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
        if not vemail:
            return None
        return True

    def valid_password(self, password):
        password = re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password)
        if password is None:
            return None
        return True

    def valid_string(self, value):
        """
            checks if value in data is empty
        """
        if not isinstance(value, str):
            return None
        return True

    def blank_key(self):
        pass
