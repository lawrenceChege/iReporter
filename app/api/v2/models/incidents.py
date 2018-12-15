"""
    This module handles the models for incidents
"""
import smtplib
import datetime
import psycopg2
from flask import request
from twilio.rest import Client
from flask_jwt_extended import get_jwt_identity
from migrations import DbModel



class IncidentsModel(DbModel):
    """
        This class handles data for the redflags views
    """
    def __init__(self, record_type=None,location=None, status=None,
                images=None, video=None, title=None, comment=None, createdBy=None):
        super().__init__()
        self.createdOn = datetime.datetime.now()
        self.modifiedOn = datetime.datetime.now()
        self.record_type = record_type
        self.location = location
        self.status = status
        self.images = images
        self.video = video
        self.title = title
        self.comment = comment
        self.createdBy = self.current_user()
        self.client = Client(self.account_sid, self.auth_token)


    def find_incident_by_comment(self, comment):
        """ gets an incident from comment"""
        try:
            self.cur.execute(
                "SELECT * FROM incidents WHERE comment=%s", (comment,)
                )
            comment = self.findOne()
            return comment
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def find_incident_id(self,comment):
        """ Finds the id of the posted incident"""
        try:
            self.cur.execute(
                "SELECT incident_id FROM incidents WHERE comment=%s", (comment,)
                )
            incident_id = self.findOne().get('incident_id')
            return incident_id
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def post_incident(self):
        """
            This method saves an incident to the database
        """
        try:
            data =( self.record_type, self.location, self.images,
            self.video, self.title, self.comment, self.createdBy,
            self.createdOn,self.modifiedOn )

            self.cur.execute(
                """
                    INSERT INTO incidents (
                        record_type, location, images,
                        video, title, comment, createdBy,
                        createdOn, modifiedOn)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);
                """, data
            )
            self.commit()
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('could not save to db')
            return None

    def get_all_incidents(self):
        """
            This method returns all the posted incidents
        """
        try:
            self.cur.execute(
                "SELECT * FROM incidents"
            )
            data = self.findAll()
            return data
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def get_incident_by_id(self, incident_id):
        """
            This method retrieves an incident by id from the database.
            It takes the id of the incident as parameter and
            It returns the incident as a result
        """
        try:
            self.cur.execute(
                "SELECT * FROM incidents WHERE incident_id=%s", (incident_id,)
                )
            incident = self.findOne()
            return incident
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def check_incident_status(self, incident_id):
        """
            Checks if status has been changed
        """
        incident = self.get_incident_by_id(incident_id)
        status = incident.get('status').strip()
        if status != 'pending':
            return False
        return True

    def edit_incident(self, location, images, video, title, comment,incident_id):
        """
            This method can modify one or all the fields of an incident
            It takes the id of the incident as the parameter and,
            It returns the updated incident as a result.
        """
        try:
            self.cur.execute(
                """
                UPDATE incidents
                SET
                location = %s,
                images = %s,
                video = %s,
                title = %s,
                comment = %s,
                modifiedOn = %s

                WHERE incident_id = %s;
                """,(location, images, video, title, comment, self.modifiedOn, incident_id,
                )
                )
            self.commit()
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def delete_incident(self, incident_id):
        """
            This method removes an incident by id from the database.
            It takes an id of the incident as parameter and,
            It returns the list of incidents.
        """
        try:
            self.cur.execute(
                "DELETE FROM incidents WHERE incident_id=%s", (incident_id,)
                )
            self.commit()
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def edit_incident_comment(self, comment, incident_id):
        """
            This method modifies the description field of an incident.
            It takes an id as parameter and,
            It returns The updated incident as a result.

        """
        try:
            self.cur.execute(
                """
                UPDATE incidents
                SET comment = %s
                WHERE incident_id = %s;
                """, (comment, incident_id)
                )
            self.commit()
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def edit_location(self, location, incident_id):
        """
            This method modifies the location field of an incident.
            It takes an id as the parameter.
            It returns the updated incident.
        """
        try:
            self.cur.execute(
                """
                UPDATE incidents
                SET location = %s
                WHERE incident_id = %s;
                """, (location, incident_id)
                )
            self.commit()
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def edit_status(self, status, incident_id):
        """
            This method modifies the status field of an incident.
            It takes an id as the parameter.
            It returns the updated incident.
        """
        try:
            self.cur.execute(
                """
                UPDATE incidents
                SET status = %s
                WHERE incident_id = %s;
                """, (status, incident_id)
                )
            self.commit()
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def send_email(self, email, status):
        """
            sends an email to a user
        """
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.set_debuglevel(1)
        server.login("ireporteradmn@gmail.com", "Qas!@#$%^&*")
        msg = 'Your incident status has been changed to {}'.format(status)
        server.sendmail("ireporteradmn@gmail.com", email, msg)
        server.quit()

    def send_sms(self, phone, status):
        """
            sends an sms notification to user
        """

        msg = 'Your incident status has been changed to {}'.format(status)

        message = self.client.messages.create(
            to= '+254'+ phone,
            from_=self.admin_phone,
            body=msg)


    def current_user(self):
        """
            This method gets the logged in user from jwt token.
            It returns the username.
        """
        self.user = get_jwt_identity()
        return self.user
