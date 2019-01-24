import psycopg2
import os


from dotenv import load_dotenv


load_dotenv()
DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASE_TEST_URL = os.environ.get('DATABASE_TEST_URL')
 

def db_con():
    try:
        con = psycopg2.connect(DATABASE_URL)

    except Exception:
        print("Unable to make database connection")
    
    return con

def db_con_test():
    try:
        con = psycopg2.connect(DATABASE_TEST_URL)

    except Exception:
        print("Unable to make database connection")
    
    return con

    
    

