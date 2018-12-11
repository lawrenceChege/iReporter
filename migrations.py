""" This module holds the database migrations """
import os
import psycopg2
from psycopg2.extras import RealDictCursor

HEROKU_DB_URL = 'postgres://gqpylxymapzcup:ebd641e7c5bd2116a79f179a869557f684818b0df68a0379a528330987886192@ec2-184-72-239-186.compute-1.amazonaws.com:5432/d2hukbh74b0mkk'
DATABASE_URL = 'postgresql://localhost/ireporter?user=postgres&password=12345678'
TEST_DATABASE_URL = 'postgresql://localhost/ireporter_test?user=postgres&password=12345678'
CONNECTION_CREDS = {
    "host": os.getenv('DB_HOST'),    
    "database": os.getenv('DB_NAME'),
    "user": os.getenv('DB_USER'),
    "password": os.getenv('DB_PASSWORD')
}
TEST_CONNECTION_CREDS = {
    "host": os.getenv('TEST_DB_HOST'),    
    "database": os.getenv('TEST_DB_NAME'),
    "user": os.getenv('TEST_DB_USER'),
    "password": os.getenv('TEST_DB_PASSWORD')
}

class DbModel():
    """
        consists of methods to connect and query from db
    """
    def __init__(self, db):
        self.db_url = DATABASE_URL
        self.db_test_url = TEST_DATABASE_URL
        self.db_con_creds = CONNECTION_CREDS
        self.db_heroku = HEROKU_DB_URL
        self.db_test_con_creds = TEST_CONNECTION_CREDS
        self.conn = self.choose_db(db)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def connection(self, *args, **url):
        """
            connect to postgres database
        """
        conn = psycopg2.connect(url)
        return conn



    def init_db(self):
        """
            connect to ireporter database
        """
        try:
            print("connecting to main  db...\n")
            try:
                conn = connection(self.db_heroku)
                print('connected to heroku db\n')
                return conn
            except:
                conn = psycopg2.connect(
                    'postgresql://localhost/ireporter?user=postgres&password=12345678')
                print('connected to db\n')
                return conn
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('error connecting to db\n')

    def init_test_db(self):
        """
            connect to test db
        """
        try:
            print("connecting to test db...\n")
            try:
                conn = connection(self.db_test_url)
                print('connected to test db\n')
                return conn
            except:
                conn = psycopg2.connect(
                    'postgresql://localhost/ireporter_test?user=postgres&password=12345678')
                print('connected to test db\n')
                return conn
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('error connecting to test db\n')

    def choose_db(self,db):
        """ choose database to connect to """
        if db == "main":
            conn = self.init_db()
            return conn
        elif db == "test":
            conn = self.init_test_db()
            return conn

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



    


    