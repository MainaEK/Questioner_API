from werkzeug.security import generate_password_hash

create_tables =["""
CREATE TABLE IF NOT EXISTS users (
user_id SERIAL PRIMARY KEY NOT NULL,
firstname VARCHAR(250) NOT NULL,
lastname VARCHAR(250) NOT NULL,
othername VARCHAR(250) NULL,
username VARCHAR(250) NOT NULL,
phone_number VARCHAR(250) NULL,
email VARCHAR(250) NOT NULL,
password VARCHAR(250) NOT NULL,
registered_on TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
admin BOOLEAN NOT NULL DEFAULT FALSE
)
""",
"""
CREATE TABLE IF NOT EXISTS meetups (
meetup_id SERIAL PRIMARY KEY NOT NULL,
topic VARCHAR(250) NOT NULL,
location VARCHAR(250) NOT NULL,
happening_on TIMESTAMP WITHOUT TIME ZONE NOT NULL,
created_on TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
modified_on TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
images TEXT [],
tags TEXT []
)
""",
"""
CREATE TABLE IF NOT EXISTS questions (
question_id SERIAL PRIMARY KEY NOT NULL,
title VARCHAR(250) NULL,
body VARCHAR(250) NOT NULL,
votes INTEGER NOT NULL DEFAULT 0,
meetup_id INTEGER NOT NULL,
user_id INTEGER [],
created_on TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
modified_on TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
FOREIGN KEY (meetup_id) REFERENCES meetups(meetup_id)
)
""",
"""
CREATE TABLE IF NOT EXISTS comments (
comment_id SERIAL PRIMARY KEY NOT NULL,
body VARCHAR(250) NULL,
question_id INTEGER NOT NULL,
user_id INTEGER NOT NULL,
created_at TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
modified_on TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
FOREIGN KEY (question_id) REFERENCES questions(question_id),
FOREIGN KEY (user_id) REFERENCES users(user_id)
)
""",
"""
CREATE TABLE IF NOT EXISTS rsvps (
meetup_id INTEGER NOT NULL,
user_id INTEGER NOT NULL,
rsvp VARCHAR(10),
created_at TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
modified_on TIMESTAMP WITHOUT TIME ZONE \
DEFAULT (NOW() AT TIME ZONE 'utc'),
PRIMARY KEY (meetup_id, user_id),
FOREIGN KEY (meetup_id) REFERENCES meetups(meetup_id),
FOREIGN KEY (user_id) REFERENCES users(user_id)
)
"""
]

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
    