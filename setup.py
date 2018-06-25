from distutils.core import setup

requirements = [
    'peewee',
    'bcrypt',
    'termcolor',
    'colorama',
    'pyperclip'
]

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

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
    classifiers = [
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Documentation',
        'Topic :: Utilities'
    ],
)
