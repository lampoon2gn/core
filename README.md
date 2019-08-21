# CORE

## SETUP:
* `$ cd core`
* `$ pip3 install requirements.txt`
* `$ FLASK_APP=app.py FLASK_DEBUG=1 flask run`

## How to update database:
* `$ python3 manage.py db migrate`
* `$ python3 manage.py db upgrade`

## API endpoints:
* `localhost:5000/api/ping` with method `GET`
* `localhost:5000/api/v1/analyze` with method `POST`
