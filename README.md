#  Yalantis Python School


## Stack of technologies 

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [python-dotenv](https://pypi.org/project/python-dotenv/) - for production
- [pytest](https://docs.pytest.org/en/6.2.x/contents.html) - for tests

## Installation

```
git clone https://github.com/Oleksandr-Khomych/Yalantis-Test-Task.git
```

API requires [Python](https://www.python.org) version 3.9+

Install the dependencies.

```sh
pip install -r requirements.txt
```

Start project file locally
```
python wsgi.py
```

Verify the deployment by navigating to your server address in
your preferred browser.

```
127.0.0.1:5000
```

## Actions

### - GET /

### - POST /create
  
Field | Type
------------ | -------------
***name*** | **reqired**, str
***start_date*** | **reqired**, date('%Y-%m-%d'), example "2020-04-20"
***end_date*** | **reqired**, date('%Y-%m-%d'), example "2021-05-30"
***lectures_count*** | **reqired**, integer number greater than zero
**The parameter start_date must be less than end_date**

### - GET /catalog

### - GET /course/{***course_id***}

### - PATCH /course/{***course_id***}
  
Field | Type
------------ | -------------
***name*** | **optional**, str
***start_date*** | **optional**, date('%Y-%m-%d'), example "2020-04-20"
***end_date*** | **optional**, date('%Y-%m-%d'), example "2021-05-30"
***lectures_count*** | **optional**, integer number greater than zero
**There must be at least one argument for a successful query**

**The parameter start_date must be less than end_date**

### - DELETE /course/{***course_id***}

### - GET /search
Field | Type
------------ | -------------
***name*** | **reqired**, str
***start_date[gte]*** | **optional**, date('%Y-%m-%d'), example "2020-04-20"
***start_date[lte]*** | **optional**, date('%Y-%m-%d'), example "2021-05-30"
***end_date[gte]*** | **optional**, date('%Y-%m-%d'), example "2020-04-20"
***end_date[lte]*** | **optional**, date('%Y-%m-%d'), example "2021-05-30"

## Host on AWS

```
http://ec2-18-219-122-41.us-east-2.compute.amazonaws.com:8001/
```

It is even allowed to click:)