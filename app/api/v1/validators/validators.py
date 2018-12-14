""" This module does validation for data input in incidents """
import re

class Validate():
    """
        methods for validatin incidents input data
    """

    def valid_email(self, email):
        self.vemail = re.match(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
        if not self.vemail:
            return None
        return True

    def valid_password(self, password):
        self.password = re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password)
        if self.password is None:
            return None
        return True
    
    def valid_string(self, value):
        """
            checks if value in data is empty
        """
        self.value = value
        if not isinstance(self.value, str):
            return None
        return True


    