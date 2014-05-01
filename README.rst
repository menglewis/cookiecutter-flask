cookiecutter-flask
=======================

A cookiecutter_ template for Flask. This is simply a template that I have found useful in starting a Flask project.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Features
---------

* Uses Blueprints and Application Factories
* Comes with a simple user model that can easily be extended
* Uses Flask-SQLAlchemy for models
* Uses Flask-Migrate for database migrations
* Simple Bootstrap 3 base templates

Usage
------

Install Cookiecutter::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/menglewis/cookiecutter-flask.git

You'll be prompted for some questions, answer them, then it will create a Flask project for you.

Enter the directory for the project::

    $ cd project-name

To get it running locally, start by creating a virtualenv for the project and activating it::

    $ mkvirtualenv flask-project

Or without using virtualenvwrapper::

    $ virtualenv venv
    $ source venv/bin/activate

Install dependencies::

    $ pip install -r requirements.txt

manage.py
------

There are various commands available from manage.py

To create the initial database run::

    $ python manage.py createdb

To create a user from the command line use the following command and enter a username and password::

    $ python manage.py createuser

The python shell loads with the app, db, and User objects in the context::

    $ python manage.py shell

To run the development server use runserver::

    $ python manage.py runserver

Database migrations are handled with the db command

When a database migration needs to be made. Run the following commmands::

    $ python manage.py db migrate

This will create a migration script. Then run the following to apply the migration::

    $ python manage.py db upgrade

For a full migration command reference, run ``python manage.py db --help``.

To run the tests, you need to have the test requirements installed and run the management command::

    $ pip install -r requirements/test.txt
    $ python manage.py test
