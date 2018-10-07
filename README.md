# Flask Pytest Intro

Unit tests should be run after lint in your Continuous Integration.

## Validated On
Ubuntu 18.04</br>
Python 3.6.6

## Setup
From the project's root directory:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install wheel
$ pip install -r requirements
$ pip install -e .
```

## Pytest
From the project's root directory:
```
$ pytest
```
Check code coverage:
```
$ coverage run --source flask_pytest_intro -m pytest
$ coverage report -m
```
