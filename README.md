# Questioner_API

[![Build Status](https://travis-ci.org/erick-maina/Questioner_API.svg?branch=develop)](https://travis-ci.com/erick-maina/Questioner_API)
[![Coverage Status](https://coveralls.io/repos/github/erick-maina/Questioner_API/badge.svg?branch=develop)](https://coveralls.io/github/erick-maina/Questioner_API?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/eec9837dfd5cf2c5312e/maintainability)](https://codeclimate.com/github/erick-maina/Questioner-API/maintainability)

A questioner is a platform for crowd-sourcing questions for a meetup. It helps the meetup organizer prioritize  questions to be answered. Other users can vote on asked questions and they bubble to the top  or bottom of the log.

## Prerequisites
- Python 3.6 
- Postman


## Installation
1. Clone this repository :

	```
    $ git clone https://github.com/erick-maina/Questioner_API.git
    ```

2. CD into the project folder on your machine

	```
    $ cd Questioner_API
    ```

3. Create a virtual environment

    ```
    $ python3 -m venv venv
    ```

4. Activate the virtual environment

	```
    $ source venv/bin/activate
    ```

5. Install the dependencies from the requirements file

	```
    $ pip install -r requirements.txt
    $ pip install python-dotenv
    ```

6. Run the application

    ```
    python3 run.py
    ```

## Testing API endpoint

| Endpoint                             | HTTP Verb   | Functionality           |
| ------------------------------------ | ----------- | ----------------------- |    
| /api/v1/meetups                  | POST        | Create a meetup record       |
| /api/v1/meetups/<meetup_id>           | GET         | Fetch a specific meetup record |
| /api/v1/meetups/<meetup_id>           | DELETE         | Deleting a specific meetup record |
| /api/v1/meeetups/upcoming           | GET         | Fetch all upcoming meetup records       |
| /api/v1/meetups/<meetup_id>/rsvps    | POST        | Create a rsvp for a specific meetup   |
| /api/v1/meetups/<meetup_id>/tags                  | POST        | Posting a tag to a meetup      |
| /api/v1/meetups/<meetup_id>/images                  | POST        | Posting an image to a meetup  |
| /api/v1/questions                | POST        | Create a question for a specific meetup   |
| /api/v1/questions/<question_id>/upvote| PATCH       | Up-vote a specific question       |
| /api/v1/questions/<question_id>/downvote| PATCH       | Down-vote a specific question       |
| /api/v1/comments  | POST        | Making a comment on a question   |
| /api/v1/auth/signup                  | POST        | Create a user      |
| /api/v1/auth/login                  | POST        | Login a user      |


## Authors
[Eric Maina](https://github.com/erick-maina)

## License
This project is licensed under [MIT](https://github.com/erick-maina/Questioner_API/blob/develop/LICENSE) license.

## Acknowledgement
- Andela Workshops
- Team members