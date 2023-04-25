import psycopg2

DATABASE = 'postgres'
USER = 'postgres'
NAME = 'supermarket'
HOST = 'localhost'
PASSWORD = 123
PORT = 5432

def connect():
    conn = psycopg2.connect(database = NAME,
                            user = USER, 
                            host= HOST,
                            password = PASSWORD,
                            port = PORT)
    return conn