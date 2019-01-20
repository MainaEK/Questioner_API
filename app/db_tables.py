from werkzeug.security import generate_password_hash

create_tables =["""
CREATE TABLE IF NOT EXISTS users (
user_id SERIAL PRIMARY KEY NOT NULL,
firstname VARCHAR(250) NOT NULL,
lastname VARCHAR(250) NOT NULL,
othername VARCHAR(250) NULL,
username VARCHAR(250) NOT NULL,
phonenumber VARCHAR(250) NULL,
email VARCHAR(250) NOT NULL,
password VARCHAR(250) NOT NULL,
registered TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
admin BOOLEAN NOT NULL DEFAULT FALSE
)
""",
"""
CREATE TABLE IF NOT EXISTS meetups (
m_id SERIAL PRIMARY KEY NOT NULL,
topic VARCHAR(250) NOT NULL,
location VARCHAR(250) NOT NULL,
happening_on TIMESTAMP WITHOUT TIME ZONE NOT NULL,
created_on TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
modified_on TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
images VARCHAR(250) NULL,
tags VARCHAR(250) NULL
)
""",
"""
CREATE TABLE IF NOT EXISTS questions (
q_id SERIAL PRIMARY KEY NOT NULL,
title VARCHAR(250) NULL,
body VARCHAR(250) NOT NULL,
votes INTEGER NOT NULL DEFAULT 0,
m_id INTEGER NOT NULL,
user_id INTEGER NOT NULL,
created_on TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
modified_on TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
FOREIGN KEY (m_id) REFERENCES meetups(m_id),
FOREIGN KEY (user_id) REFERENCES users(user_id)
)
""",
"""
CREATE TABLE IF NOT EXISTS comments (
c_id SERIAL PRIMARY KEY NOT NULL,
body VARCHAR(250) NULL,
q_id INTEGER NOT NULL,
user_id INTEGER NOT NULL,
created_at TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
modified_on TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
FOREIGN KEY (q_id) REFERENCES questions(q_id),
FOREIGN KEY (user_id) REFERENCES users(user_id)
)
""",
"""
CREATE TABLE IF NOT EXISTS rsvps (
m_id INTEGER NOT NULL,
user_id INTEGER NOT NULL,
response VARCHAR(10),
created_at TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
modified_on TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
PRIMARY KEY (m_id, user_id)
)
""",
"""
CREATE TABLE IF NOT EXISTS votes (
q_id INTEGER NOT NULL,
user_id INTEGER NOT NULL,
vote VARCHAR(10),
PRIMARY KEY (q_id, user_id)
)
"""]

def create_db(connect):
    cur = connect.cursor()
    for query in create_tables:
        cur.execute(query)
    connect.commit()


def admin(connect):
    cur = connect.cursor()
    cur.execute("INSERT INTO users (firstname, lastname, username, email, password, admin)\
        VALUES ('Eric', 'Maina', 'eric', 'admin@app.com', '{}', True)\
        ".format(generate_password_hash('Eric1234')))
    connect.commit()
    