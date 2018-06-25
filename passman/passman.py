#!/usr/bin/env python3
# don't forget : chmod +x passman.py

import bcrypt
from models import *
from helpers import *
from colorama import init
from termcolor import colored, cprint

init()

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
    new_user = False
    while new_user == False:
        clear()
        print(line)
        title("Create user")
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
        login_menu()
    else:
        login = True

    while login == False:
        clear()
        print(line)

        title("Log in")
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

def login_menu():
    clear()
    cprint(logo, 'green')

    print(line)

    print(colored('l', 'magenta') + ") " + 'log in with an existing user')
    print(colored('c', 'magenta') + ") " + 'create a new user')

    action = input(colored('Action:', 'cyan') + ' [Lc] ').lower().strip()

    if action == 'c':
        create_user()

def logout():
    """Logout"""
    global current_user
    current_user = None
    cprint("User logged out", "green")
    login()

def menu_loop():
    """Show the menu"""
    choice = None

    while choice != 'q':
        clear()
        print(line)

        title("Main menu")
        for key, value in menu.items():
            print(colored(key, 'magenta') + ") " + value.__doc__)

        print(colored('q', 'yellow') + ") " + "Quit passman")

        choice = input(colored('Action:', 'cyan') + ' ').lower().strip()

        if choice in menu:
            menu[choice]()

def add_password():
    """Add a password"""
    clear()
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
            input("(press any key to continue)")

def view_passwords(search_query = None):
    """View all passwords"""

    global current_user
    passwords = Password.select().where(Password.user == current_user).order_by(Password.modified_at.desc())
    if search_query:
        passwords = passwords.where(Password.application.contains(search_query))

    clear()

    if not passwords:
        cprint("No records found...", 'yellow')

    for password in passwords:
        show_password(password)
        next_action = input(f"{colored('Action:', 'cyan')} [Nq] ").lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_password(password)

def search_passwords():
    """Search passwords by name"""
    print(line)
    query = input(f"{colored('Search', 'cyan')}: ").lower().strip()
    view_passwords(query)

def delete_password(password):
    """Delete a password"""
    if input("Are you sure? [yN] ").lower().strip() == 'y':
        password.delete_instance()
        cprint("Password successfully deleted!", "green")

def update_password(password):
    """Update a password"""
    print(colored('a', 'magenta') + ") " + f"update application: {password.application}")
    print(colored('l', 'magenta') + ") " + f"update login name: {password.login}")
    print(colored('p', 'magenta') + ") " + f"update password: {password.password}")
    print(colored('n', 'magenta') + ") " + f"update notes: {password.notes}")

menu = OrderedDict([
    ('a', add_password),
    ('v', view_passwords),
    ('s', search_passwords),
    ('l', logout)
])
