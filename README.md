# Flask + HTML Practice

## About Flask

Flask is a highly used Python micro Web Framework. It provides basic functionality to build web applications, like routing, request/response handling, etc. It's a "small" framework compared to other ones (like Django), but in many cases that's a great advantage.


## Install Instructions
Fork this repo and create a new cloud9 workspace as we do with other projects. Then follow the usual steps:

```bash
$ mkvirtualenv flask-html-practice -p /usr/bin/python3
$ pip install -r requirements.txt
```


## Running the app server

Flask framework provides, out of the box, a way to run a development web server in your local machine. Just execute the `run_app.py` script available in the project and the application will stay listening at `localhost:8080`. (Make sure to have all the requirements previously installed)

```bash
$ python run_app.py
```


## Running tests

Tests are split among several functions. You can run them all together doing `pytest tests.py` or select individual based on keyword expressions like `pytest -k 'test_1' tests.py`.


## Tasks

The goal for this practice is to implement a simple login form with username and password, introducing some HTML content and some extra Flask functionalities apart from the ones used in the last practice (i.e: redirect function)

The first three views are done for you as an example. You'll have to reply the same given functionality but in a single view combining actions for both GET and POST methods.
