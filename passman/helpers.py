import os

from colorama import init
from termcolor import colored, cprint
import pyperclip

logo = """\
 _____ _____ _____ _____ _____ _____ _____
|  _  |  _  |   __|   __|     |  _  |   | |
|   __|     |__   |__   | | | |     | | | |
|__|  |__|__|_____|_____|_|_|_|__|__|_|___|
"""

line = "\n" + ('=' * 25) + "\n"

def print_errors(errors):
    if len(errors) > 0:
        cprint("** Error - entry cannot be saved", 'red')
        for error in errors:
            cprint(f"** {error}", 'red')
        print(line)
        return True
    else:
        return False

def title(title):
    cprint(title, "magenta", attrs=['bold'])

def show_password(password):
    modified_at = password.modified_at.strftime('%B %d, %Y')

    print(line)

    print(f"""\
{colored('Application Name', 'yellow')}: {password.application}
{colored('Login Credentials', 'yellow')}: {password.login}
{colored('Password', 'yellow')}: {password.password}
{colored('Notes', 'yellow')}: {password.notes}
{colored('Last Modified', 'yellow')}: {modified_at}
{colored('* Current password copied to clipboard', 'green')}
    """)

    pyperclip.copy(password.password)

    print(f"""\
{colored('n', 'magenta')}) next password
{colored('u', 'magenta')}) update password
{colored('d', 'magenta')}) delete password
{colored('q', 'yellow')}) return to main menu
    """)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
