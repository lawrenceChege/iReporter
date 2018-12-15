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

    def check_record_type(self, record_type):
        """ 
            checks if record type is redflag or intervention
        """
        self.incident = record_type.lower().strip()

        if self.incident == 'redflag' or self.incident == 'red-flag'or self.incident == 'red_flag' or self.incident == 'intervention':
            return None
        return self.incident

    def check_status(self, status):
        """
            checks if status is under-investigation, resolved, rejected or pending
        """
        self.incident = status.lower().strip()

        if self.incident == 'resolved' or self.incident == 'rejected'or self.incident == 'under-investigation' or self.incident == 'pending':
            return None
        return self.incident

    def check_loaction(self,location):
        """
            matches inputs to corect location
        """
        self.location = re.match(r"(^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$)", location)
        if self.location is None:
            return None
        return True

    def check_phone(self,phone):
        """
            validate phone number
        """
        self.phone = re.match(r'^[7]\d{8,8}$', phone)
        if self.phone is None:
            return None
        return True