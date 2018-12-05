""" This module holds the database migrations """
import os
import psycopg2

DATABASE_URL = os.getenv('DATABASE_URL')
TEST_DATABASE_URL = os.getenv('TEST_DATABASE_URL')
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

def connection(*args, **url):
    """
        connect to postgres database
    """
    conn = psycopg2.connect(url)
    return conn

def init_db():
    """
        connect to ireporter database
    """
    try:
        print("conecting to ireporter database ...")
        try:
            conn = connection(**CONNECTION_CREDS)
            print("connected to db")
            return conn
        except :
            conn = connection(DATABASE_URL)
            print("connected to db")
            return conn
    except:
        print("connection to database failed")

def init_test_db():
    """
        connect to test db
    """
    try:
        print("conecting to TEST database ...")
        try:
            conn = connection(**TEST_CONNECTION_CREDS)
            print("connected to tet db")
            return conn
        except :
            conn = connection(TEST_DATABASE_URL)
            print("connected to test db")
            return conn
    except:
        print("connection to test database failed")

def create_tables():
    """
        create tables in the database
    """
    commands = (
        """
            CREATE TABLE IF NOT EXISTS users(
                user_id SERIAL PRIMARY KEY,
                firstname CHAR(20),
                lastname CHAR(20),
                othernames CHAR(20),
                username VARCHAR(20) NOT NULL unique,
                email VARCHAR(50) NOT NULL unique,
                passord VARCHAR(100) NOT NULL,
                registered DATE NOT NULL DEFAULT CURRENT_DATE,
                isAdmin BOOLEAN NOT NULL DEFAULT FALSE
            )
        """,
        """
            CREATE TABLE IF NOT EXISTS incidents(
                incident_id SERIAL PRIMARY KEY,
                createdOn DATE NOT NULL DEFAULT CURRENT_DATE.
                modifiedOn DATE NOT NULL DEFAULT CURRENT-DATE,
                CREATE TYPE type AS ENUM ('red-flag', 'incident),
                location point,
                CREATE TYPE status AS ENUM ('draft', 'under investigation', 'resolved','rejected')
                images VARCHAR(80),
                video VARCHAR(80),
                title VARCHAR(100) NOT NULL,
                comment VARCHAR(250) NOT NULL unique,
                createdBy INT REFERENCES users (user_id)

            )
        """
    )
    conn = None
    test_conn = None
    try:
        test_conn = init_test_db()
        test_cur = test_conn.cursor()
        conn = init_db()
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
            test_cur.execute(command)
        cur.close()
        test_cur.close()
        conn.commit()
        test_conn.commit()
        conn.close()
        test_conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print (error)
        print('could not create tables')
    finally:
        if conn or test_conn is not None:
            conn.close()
            test_conn.close()

if __name__ == '__main__':
    create_tables()
    