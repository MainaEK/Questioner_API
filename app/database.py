import psycopg2
import os


from dotenv import load_dotenv


load_dotenv()
DATABASE_URL = os.environ.get('DATABASE_URL')


def db_con():
    try:
        con = psycopg2.connect(DATABASE_URL)

    except Exception:
        print("Unable to make database connection")
    
    return con
    

