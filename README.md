# PassMan
<img src="assets/Release-1.2.4-blue.svg">

PassMan is a super simple, Python-based **pass**word **man**agement console application. Data is managed using Peewee ORM and stored in a Sqlite3 database.

### Dependencies
* Python3
  * Check version using `$ python --version`
  * <a href="https://www.python.org/downloads/release/python-365/">Installing or upgrading to Python3</a>
* <a href="http://docs.peewee-orm.com/en/latest/">PeeWee</a>
* <a href="https://pypi.org/project/bcrypt/">Bcrypt</a>
* <a href="https://pypi.org/project/colorama/">Colorama</a>
* <a href="https://pypi.org/project/termcolor/">Termcolor</a>
* <a href="">Pyperclip</a>

### Installation and Usage
```shell
$ pip3 install passwordmanager
$ # "path/to/python path/to/passman"
$ python3 passman
```

**Notes:**  
It's helpful to alias "python" and "pip" to point towards the "python3" and "pip3" commands respectively.
```shell
$ echo "alias python=python3" > ~/.bashrc
$ echo "alias pip=pip3" > ~/.bashrc
$ # for zshell users, replace ~/.bachrc with ~/.zshrc
```

Additionally, you can alias 'passman' to the execute the entire command.

```shell
# the following works for most MacOS users:
$ echo "alias passman='python3 passman'" > ~/.bashrc
# the following works for most Windows 10 users:
$ echo "alias passman='python3 && cd \"/c/Program Files (x86)/Python36-32/Lib/site-packages/passman/__main__.py\"'" >
```

**TODO:**
* Separate main menu functions into own module
* Add feature to copy current password to clipboard
* Update/delete passwords from database

**Author:**  
Sean Pierce Sumler

**License:**  
MIT, use at your own risk

For questions and comments please <a href="https://github.com/seanpierce/passman/issues/new">raise an issue</a>. <a href="https://github.com/seanpierce/passman/compare">Pull requests</a> always welcome, too. Thanks!