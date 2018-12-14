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

    def check_record_type(self, record_type):
        """ 
            checks if record type is redflag or intervention
        """
        incident = record_type.lower().strip()

        if incident == 'redflag' or incident == 'red-flag'or incident == 'red_flag' or incident == 'intervention':
            return None
        return incident

    def check_status(self, status):
        """ 
            checks if status is under-investigation, resolved, rejected or pending
        """
        incident = status.lower().strip()

        if incident == 'resolved' or incident == 'rejected'or incident == 'under-investigation' or incident == 'pending':
            return None
        return incident