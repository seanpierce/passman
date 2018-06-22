#!/usr/bin/env python3
# don't forget : chmod +x passman.py

import bcrypt
from models import *
from colorama import init
from termcolor import colored, cprint

init()

line = "\n" + ('=' * 25) + "\n"
current_user = None

def initialize():
    """Create the database and tables if they don't already exist"""
    db.connect()
    db.create_tables([Password, User], safe = True)

def check_users():
    users = User.select()
    if not users.exists():
        create_user()


def create_user():
    """Create a new user"""
    cprint('Create a new user', 'magenta', attrs=['bold'])
    new_user = False
    while new_user == False:
        print(line)
        username = input(f"Enter a {colored('username', 'cyan')}: ")
        password = input(f"Enter a {colored('password', 'cyan')}: ")
        confirmation = input(f"Confirm {colored('password', 'cyan')}: ")

        errors = []
        if username == "":
            errors.append('Missing username')
        if password == "":
            errors.append('Missing password')
        if confirmation == "":
            errors.append('Missing password confirmation')
        if password != confirmation:
            errors.append('Password and confirmation do not match')

        if print_errors(errors) == True:
            continue

        query = User.select().where(User.username == username)
        if query.exists():
            print("Username unavailable. Please try again.")
            continue

        hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        global current_user
        current_user = User.create(
            username = username,
            password_hash = hash
        )
        cprint("User created successfully!", 'green')
        new_user = True


def login():
    global current_user
    if not current_user:
        login = False
    else:
        login = True

    while login == False:
        print(line)
        entered_username = input("Please enter your user name: ")
        entered_password = input("Please enter your master password: ")

        query = User.select().where(User.username == entered_username)
        if not query.exists():
            print("User '{}' not found".format(entered_username))
            continue

        created_user = User.get(User.username == entered_username)
        hash = bcrypt.hashpw(entered_password.encode('utf-8'), created_user.password_hash.encode('utf-8'))

        if created_user.password_hash.encode('utf-8') == hash:
            current_user = created_user
            login = True
        else:
            print("Password not valid for user '{}'".format(entered_username))
            continue

def print_errors(errors):
    if len(errors) > 0:
        cprint("** Error - entry cannot be saved", 'red')
        for error in errors:
            cprint(f"** {error}", 'red')
        print(line)
        return True
    else:
        return False

def menu_loop():
    """Show the menu"""
    choice = None

    while choice != 'q':
        print(line)
        print("Enter" + colored(" 'q' ", 'yellow') + "to quit.")
        for key, value in menu.items():
            print(colored(key, 'magenta') + ") " + value.__doc__)

        choice = input(colored('Action', 'cyan') + ': ').lower().strip()

        if choice in menu:
            menu[choice]()

def add_password():
    """Add a password"""
    print(line)

    application = input(f"Enter the {colored('application name', 'magenta')}: ")
    login = input(f"Enter the {colored('login name', 'magenta')} (email or username): ")
    password = input(f"Enter {colored('password', 'magenta')}: ")
    password_again = input(f"Confirm {colored('password', 'magenta')}: ")
    notes = input(f"(optional) Enter {colored('notes/ additional info', 'magenta')}: ")

    errors = []
    if application == "":
        errors.append('Missing application')
    if login == "":
        errors.append('Missing login')
    if password == "":
        errors.append('Missing password')
    if password_again == "":
        errors.append('Missing password confirmation')
    if password != password_again:
        errors.append('Password and confirmation do not match')

    print_errors(errors)

    if not errors:
        if input(f"{colored('Save password?', 'cyan')} [Yn] ").lower() != 'n':
            global current_user
            Password.create(
                user = current_user,
                application = application,
                login = login,
                password = password,
                notes = notes
            )
            cprint("Password saved successfully!", 'green')

def view_passwords(search_query = None):
    """View all passwords"""
    print(line)

    global current_user
    passwords = Password.select().where(Password.user == current_user).order_by(Password.modified_at.desc())
    if search_query:
        passwords = passwords.where(Password.application.contains(search_query))

    if not passwords:
        cprint("No records found...", 'yellow')

    for password in passwords:
        modified_at = password.modified_at.strftime('%B %d, %Y')
        print(line)
        print(f"{colored('Application Name', 'yellow')}: {password.application}")
        print(f"{colored('Login Credentials', 'yellow')}: {password.login}")
        print(f"{colored('Password', 'yellow')}: {password.password}")
        print(f"{colored('Notes', 'yellow')}: {password.notes}")
        print(f"{colored('Last Modified', 'yellow')}: {modified_at}")
        print("\n")
        print(f"{colored('n', 'magenta')}) for next password")
        print(f"{colored('q', 'magenta')}) return to main menu")

        next_action = input(f"{colored('Action', 'cyan')}: [Nq] ").lower().strip()
        if next_action == 'q':
            break

def search_passwords():
    """Search all passwords by application name"""
    print(line)
    query = input(f"{colored('Search', 'cyan')}: ").lower().strip()
    view_passwords(query)


def delete_password(password):
    """Delete a password"""

menu = OrderedDict([
    ('a', add_password),
    ('v', view_passwords),
    ('s', search_passwords),
    ('c', create_user)
])

if __name__ == '__main__':
    initialize()
    check_users()
    login()
    menu_loop()
