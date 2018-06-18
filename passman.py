#!/usr/bin/env python3
# don't forget : chmod +x passman.py

import datetime
from collections import OrderedDict
from peewee import *

db = SqliteDatabase('passman.db')

class Password(Model):
    application = CharField(max_length = 255)
    login = CharField(max_length = 255)
    password = CharField(max_length = 255)
    notes = TextField()
    modified_at = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = db

def initialize():
    """Create the database and tables if they don't already exist"""
    db.connect()
    db.create_tables([Password], safe = True)

def menu_loop():
    """Show the menu"""

def add_password():
    """Add a password"""

def view_passwords():
    """View all passwords"""

def delete_password(password):
    """Delete a password"""

if __name__ == '__main__':
    initialize()
    menu_loop()
