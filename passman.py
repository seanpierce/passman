#!/usr/bin/env python3
# don't forget : chmod +x passman.py

from collections import OrderedDict
import datetime
import sys

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
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()

def add_password():
    """Add a password"""
    print("Enter the application name, press ctl+d when finished.")
    data = sys.stdin.read().strip()

    if data:
        if input("Save password? [Yn] ").lower() != 'n':
            Password.create(application = data)
            print("Saved successfully!")

def view_passwords():
    """View all passwords"""

def delete_password(password):
    """Delete a password"""

menu = OrderedDict([
    ('a', add_password),
    ('v', view_passwords),
])

if __name__ == '__main__':
    initialize()
    menu_loop()
