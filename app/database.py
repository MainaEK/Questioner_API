import psycopg2
import os

from dotenv import load_dotenv
from  .db_tables import create_users,create_meetups,create_questions,create_comments,create_rsvps,create_votes

load_dotenv()
DATABASE_URL = os.environ.get('DATABASE_URL')


def db_con():
    con = psycopg2.connect(DATABASE_URL)
    return con

def create_db():
    connect = db_con()
    cursor = connect.cursor()
    cursor.execute(create_users)
    cursor.execute(create_meetups)
    cursor.execute(create_questions)
    cursor.execute(create_comments)
    cursor.execute(create_rsvps)
    cursor.execute(create_votes)
    connect.commit()
    cursor.close()


