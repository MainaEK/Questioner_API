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

def destroy():
    con = psycopg2.connect(DATABASE_TEST_URL)
    cur = con.cursor()   
    users = """DROP TABLE IF EXISTS users CASCADE;"""
    meetups = """DROP TABLE IF EXISTS meetups CASCADE;"""
    questions = """DROP TABLE IF EXISTS questions CASCADE;"""
    comments = """DROP TABLE IF EXISTS comments CASCADE;"""
    queries = [users, meetups, questions, comments]
    try:
        for query in queries:
            cur.execute(query)
        conn.commit()
    except:
        print("Fail")
    cur.close()
    

