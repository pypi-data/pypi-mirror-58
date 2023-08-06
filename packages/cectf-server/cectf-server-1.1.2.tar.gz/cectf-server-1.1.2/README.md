# cectf-server

[![Build Status](https://travis-ci.com/cectf/cectf-server.svg?branch=master)](https://travis-ci.com/cectf/cectf-server)

The backend server code for the CECTF project.

This project was built using [Python 3](https://www.python.org/) and [Flask](https://www.fullstackpython.com/flask.html), a relatively lightweight Python web server. A number of Flask plugins are also used, like [Flask-Security](https://pythonhosted.org/Flask-Security/), [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/), and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) (and of course [SQLAlchemy](https://www.sqlalchemy.org/)). [MariaDB](https://mariadb.org/) (an open source MySQL implementation) is used as the database.

cectf-server currently handles all API requests from the [cectf-fronted](https://github.com/cectf/cectf-frontend) client, including user authentication, administrative actions from the UI dashboard, and of course the actual CTF.

## Installation

Navigate to the project repository and run `./setup_workspace.sh`. This will set up the python virtual environment and install the python dependencies.

You will need to install MariaDB (https://mariadb.com/downloads/#aptyum) and have it running on localhost. For testing purposes, the user `travis` with no password needs to be created (`CREATE USER 'travis'@'localhost' IDENTIFIED BY '';`). 

Run `db_setup.sh` to set up the `test` database. This will create all the necessary tables and insert some dummy data.

## CLI

There are a handful of administration tools available in the Flask CLI. To access it, run these commands to activate the virtual environment, then set up the environment variables required to target the correct Flask application:

```
source venv/bin/activate
export FLASK_APP=cectf_server
export FLASK_ENV=development
```

Run `flask --help` for a list of available Flask commands. 

## Development Deployment

After setting up the Flask CLI as described above, you can run `flask run` to launch the development server. It is configured to run on `http://127.0.0.1:5001` by default. This can be useful to inspect the API manually, but I found it difficult to use this development server with the [cectf-fronted](https://github.com/cectf/cectf-frontend) client.

I recommend setting up nginx to host both cectf-server and [cectf-fronted](https://github.com/cectf/cectf-frontend) simultaneously. cectf-server can be deployed using uWSGI, a gateway protocol that allows web servers to communicate with generic web applications.

Run `run.sh` to launch the Flask server as a uWSGI application. The configuration for this deployment can be found in `dev_deploy/uwsgi.ini`. It is currently configured to connect to the socket file `dev_deploy/cectf_server.sock`.

You will need to install nginx on your machine, then fill out the `dev_deploy/nginx.conf` file and add it to your nginx installation. 

## Configuration

Configuration can be done by adding variables to `instance/config.py`. Here is a sample configuration file:

```
SECRET_KEY = 'dev'
SECURITY_PASSWORD_SALT = 'salty'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://travis@localhost/dev'
CECTF_PRODUCTION = False
```

## Testing

There are some additional dependencies required for testing. Enter the virtual environment, then run `pip install pytest coverage` to install them.

You will need to run `pip install -e .` to install the project in the local virtual environment (the `-e` ensures that it is updated as the project is modified). This allows `pytest` to import the project. This step only needs to be performed once.

Run `pytest` to run all tests, or `pytest tests/test_file.py` to run a specific test file.

To generate a code coverage report, run `coverage run -m pytest` or `coverage run -m pytest tests/test_file.py`. `coverage` will use `pytest` to run all the tests, then store the coverage data in a `.coverage` file. Run `coverage report` to get the report in the command line, or run `coverage html` to generate an interactive HTML page in `htmlcov/index.html`.

## Releasing

This project is managed by [Travis CI](https://travis-ci.com/cectf/cectf-server). Any commits to any branch (specifically `dev`) are tested automatically.

To cut a release of the project:

* Ensure the `dev` branch is up to date and has been pushed and tested by [Travis CI](https://travis-ci.com/cectf/cectf-server).
* Merge `dev` into `master`.
* Open `setup.py`, find the line that says `version='a.b.c',`, and increment it to the next minor (or major) version number.
* Commit your change.
* Run `git tag -a <a.b.c> -m "A quick summary of what is new in this release"`, where `<a.b.c>` is your new version number, and the commit message is meaningful.
* Run `git push origin master --tag` to push your changes to master as well as your new tag.
* Ensure that the [Travis CI](https://travis-ci.com/cectf/cectf-server) completes successfully. 
* Check that a new release was uploaded to [PyPI](https://pypi.org/project/cectf-server/).

My [production deployment](https://ctf.chiquito.us) uses the latest tag on [PyPI](https://pypi.org/project/cectf-server/) to build a docker image which is then deployed on a cluster of Raspberry Pis.