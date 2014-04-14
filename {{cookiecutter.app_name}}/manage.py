#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
try:
   input = raw_input
except NameError:
   pass

from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import MigrateCommand

from {{cookiecutter.app_name}} import create_app
from {{cookiecutter.app_name}}.auth.models import User
from {{cookiecutter.app_name}}.settings import DevConfig, ProdConfig
from {{cookiecutter.app_name}} import db

if os.environ.get("{{cookiecutter.app_name | upper}}_ENV") == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)

manager = Manager(app)
TEST_CMD = "nosetests"

def _make_context():
    '''Return context dict for a shell session so you can access
    app, db, and the User model by default.
    '''
    return {'app': app, 'db': db, 'User': User}

@manager.command
def test():
    '''Run the tests.'''
    status = subprocess.call(TEST_CMD, shell=True)
    sys.exit(status)

@manager.command
def createdb():
    db.create_all()

@manager.command
def createuser():
    """Register a new user"""
    print("Username:")
    username = input()
    from getpass import getpass
    password = getpass()
    password2 = getpass(prompt='Confirm: ')
    if password != password2:
        import sys
        sys.exit('Error: passwords do not match')
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    print('User {0} was registered!'.format(username))

manager.add_command("runserver", Server())
manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()