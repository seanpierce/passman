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

    print(f"{colored('Application Name', 'yellow')}: {password.application}")
    print(f"{colored('Login Credentials', 'yellow')}: {password.login}")
    print(f"{colored('Password', 'yellow')}: {password.password}")
    print(f"{colored('Notes', 'yellow')}: {password.notes}")
    print(f"{colored('Last Modified', 'yellow')}: {modified_at}")

    print("\n")
    print("* Current password copied to clipboard")
    pyperclip.copy(password.password)
    print("\n")

    print(f"{colored('n', 'magenta')}) for next password")
    print(f"{colored('q', 'magenta')}) return to main menu")
