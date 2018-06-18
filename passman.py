#!/usr/bin/env python3
# don't forget : chmod +x passman.py

from collections import OrderedDict
import datetime
import sys

from peewee import *

db = SqliteDatabase('passman.db')

class BaseModel(Model):
    class Meta:
        database = db

class Password(BaseModel):
    application = CharField(max_length = 255)
    login = CharField(max_length = 255)
    password = CharField(max_length = 255)
    notes = TextField(null = False)
    modified_at = DateTimeField(default = datetime.datetime.now)

def initialize():
    """Create the database and tables if they don't already exist"""
    db.connect()
    db.create_tables([Password], safe = True)

def menu_loop():
    """Show the menu"""
    choice = None

    print('_'*25)

    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()

def add_password():
    """Add a password"""
    application = input("Enter the application name: ")
    login = input("Enter the login name (email or username): ")
    password = input("Enter password: ")
    password_again = input("Confirm password: ")
    print("(optional) Enter notes/ additional info, press ctl+d when finished. ")
    notes = sys.stdin.read().strip()

    errors = []
    if application == "":
        error.append('Missing application')
    if login == "":
        error.append('Missing login')
    if password == "":
        error.append('Missing password')
    if password_again == "":
        error.append('Missing password confirmation')
    if password != password_again:
        error.append('Password and confirmation do not match')

    if errors.size:
        print("Error - Password cannot be saved: ")
        for error in errors:
            print(error)

    if not errors:
        if input("Save password? [Yn] ").lower() != 'n':
            Password.create(
                application = application,
                login = login,
                password = password,
                notes = notes
            )
            print("Saved successfully!")

def view_passwords(search_query = None):
    """View all passwords"""
    passwords = Password.select().order_by(Password.modified_at.desc())
    if search_query:
        passwords = passwords.where(Password.application.contains(search_query))

    for password in passwords:
        modified_at = password.modified_at.strftime('%A %B %d, %Y %I:%M%p')
        print(modified_at)
        print('='*len(modified_at))
        print(password.application)
        print('n) for next password')
        print('q) return to main menu')

        next_action = input("Action: [Nq] ").lower().strip()
        if next_action == 'q':
            break

def search_passwords():
    """Search all passwords by application name"""
    query = input("Search: ").lower().strip()
    view_passwords(query)


def delete_password(password):
    """Delete a password"""

menu = OrderedDict([
    ('a', add_password),
    ('v', view_passwords),
    ('s', search_passwords),
])

if __name__ == '__main__':
    initialize()
    menu_loop()
