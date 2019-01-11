# Questioner

Badges
------

[![Build Status](https://travis-ci.org/bencyn/Questioner.svg?branch=develop)](https://travis-ci.org/bencyn/Questioner)  [![Coverage Status](https://coveralls.io/repos/github/bencyn/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/bencyn/Questioner?branch=develop) [![Code Climate](https://codeclimate.com/github/codeclimate/codeclimate/badges/gpa.svg)](https://codeclimate.com/github/bencyn/Questioner)


Overview
--------
Questioner is a questions crowd-source for meetups.The platform helps meetup organizer priotize questions to be answered.Other users can vote on asked questions.

This project is managed using a pivotal tracker board. [View the board here](https://www.pivotaltracker.com/n/projects/2235259)

<!-- Find the documentation [here](https://documenter.getpostman.com/view/5582682/RznFpxuQ) -->

<!-- [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://questioner-api-version1.herokuapp.com/api/v1/) -->

<!-- [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/71ff9e20905a7f90c3a6) -->

Features
-----------------------
1. Users can create an account and log in.
2. Users can post questions.
3. Users can delete the questions they've posted.
4. Users can post answers.
5. Users can view the answers to questions.
6. Uses can accept an answer out of all the answers to his or her question as the preferred answer.
7. Users can upvote or downvote an answer.
8. Users can comment on an answer.
9. Users can fetch all questions he or she has ever asked on the platform.
10. Users can search for questions on the platform.
11. Users can view the questions with the most answers.

Pre-requisites
----------------------
1. Python3
2. Flask
3. Flask restplus
4. Postman

Getting started
--------------------
1. Clone this repository
```
    https://github.com/bencyn/Questioner.git
```

2. Navigate to the cloned repository
```
    cd Questioner
```

Installation
---------------------------------
1. Create a virtual environment
```
    virtualenv -p python3 venv
```

2. Activate the virtual environment
```
    source venv/bin/activate
```

3. Install git
```
    sudo apt-get install git-all
```

4. Switch to 'develop' branch
```
    git checkout develop
```

5. Install requirements
```
    pip install -r requirements.txt
```
Run the application
---------------------------------
```
    python3 run.py
```

When you run this application, you can test the following API endpoints using postman
-----------------------------------------------

| Endpoint | Functionality |
----------|---------------
POST/meetups | Create a meetup record
GET/meetups/&lt;meetup-id&gt; | Fetch a specific meetup record
GET /meetups/upcoming/ | Fetch all upcoming meetup records
POST /meetups/&lt;question-id&lt;questions | Create a question for a specific meetup
PATCH /questions/&lt;question-id&gt;/upvote | Upvote (increase votes by 1) a specific question
PATCH /questions/&lt;question-id&gt;/downvote | Downvote (decrease votes by 1) a specific question
POST /meetups/&lt;meetup-id&gt;/rsvps | Respond to meetup RSVP
POST /users | Create a user account
GET  /users/all | Fetch users
GET  /users/&lt;user-id&gt | Get a specific user account


Authors
-----------------------------
**Benson Njung'e** - _Initial work_-[becnyn](https://github.com/bencyn/Questioner)

Acknowledgements
-------------------------------
1. Andela Workshops
2. Team members



