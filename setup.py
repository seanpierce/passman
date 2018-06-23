from distutils.core import setup

requirements = [
    'peewee',
    'bcrypt',
    'termcolor',
    'colorama',
    'pyperclip'
]

setup(
    name = 'passwordmanager',
    version = '1.3.0',
    packages = ['passman',],
    install_requires = requirements,
    license = 'Creative Commons Attribution-Noncommercial-Share Alike license',
    description = 'A super simple password management app',
    long_description = open('readme.txt').read(),
    url = 'https://github.com/seanpierce/passman',
    author = 'Sean Pierce Sumler',
    entry_points = {
        'console_scripts': [
            'passman = __main__'
        ]
    },
)
