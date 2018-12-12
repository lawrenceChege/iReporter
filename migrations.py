""" This module holds the database migrations """
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import current_app

class DbModel():
    """
        consists of methods to connect and query from db
    """

    def __init__(self):
        self.db_url = current_app.config['DATABASE_URL']
        self.db = current_app.config['DATABASE']
        self.conn = self.init_db()
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def connection(self, url):
        """
            connect to postgres database
        """
        try:
            conn = psycopg2.connect(url)
            return conn
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('error connecting to db\n')

    def init_db(self):
        """
            connect to ireporter database
        """
        try:
            if self.db:
                print("connecting to actual db...\n") 
                conn = self.connection(self.db)
                self.cur = conn.cursor(cursor_factory=RealDictCursor)
            print("connecting to db...\n")            
            conn = self.connection(self.db_url)
            self.cur = conn.cursor(cursor_factory=RealDictCursor)
            print(self.db_url)
            print('connected to db\n')
            return conn
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('error connecting to db\n')

   
    def create_tables(self):
        """
            create tables in the database
        """
        commands = (
            """
                CREATE TABLE IF NOT EXISTS users(
                    user_id SERIAL PRIMARY KEY NOT NULL,
                    firstname CHAR(20),
                    lastname CHAR(20),
                    othernames CHAR(20),
                    username VARCHAR(20) NOT NULL unique,
                    email VARCHAR(50) NOT NULL unique,
                    phoneNumber INT,
                    password VARCHAR(100) NOT NULL,
                    registered DATE NOT NULL ,
                    isAdmin BOOLEAN NOT NULL DEFAULT FALSE
                )
            """,
            """
                CREATE TABLE IF NOT EXISTS incidents(
                    incident_id SERIAL PRIMARY KEY NOT NULL,
                    createdOn VARCHAR(50) NOT NULL ,
                    modifiedOn VARCHAR(50) NOT NULL,
                    record_type CHAR(20) NOT NULL,
                    location VARCHAR(50),
                    status CHAR(20) NOT NULL DEFAULT 'pending',
                    images VARCHAR(80),
                    video VARCHAR(80),
                    title VARCHAR(100) NOT NULL,
                    comment VARCHAR(250) NOT NULL unique,
                    createdBy INT REFERENCES users (user_id)

                )
            """
        )
        
               
        try:
            for command in commands:
                self.cur.execute(command)                
                print('creating table ..\n')
            self.commit()
            self.close()      

        except (Exception, psycopg2.DatabaseError) as error:
            print (error)
            print('could not create tables\n')
        finally:
            if self.conn is not None:
                self.conn.close()

    

    def drop_tables(self, table):
        """ drop existing tables """
        try: 
            self.cur.execute("DROP TABLE IF EXISTS"+ table)
            self.commit()
            self.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print (error)
            print('could not drop tables\n')
        finally:
            if self.conn is not None:
                self.close()


    def commit(self):
        """
        commit changes to the db
        """
        self.conn.commit()

    def close(self):
        """
            close the cursor and the connection
        """
        self.cur.close()
        self.conn.close()

    def findOne(self):
        """ return one item from query"""
        return self.cur.fetchone()

    def findAll(self):
        """ return all items from query"""
        return self.cur.fetchall()



    


    
