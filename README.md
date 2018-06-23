# PassMan
<img src="assets/Release-1.3.0-blue.svg">

PassMan is a super simple, Python-based **pass**word **man**agement console application. Data is managed using Peewee ORM and stored in a Sqlite3 database.

### Dependencies
* Python3
  * Check version using `$ python --version`
  * <a href="https://www.python.org/downloads/release/python-365/">Installing or upgrading to Python3</a>
* <a href="http://docs.peewee-orm.com/en/latest/">PeeWee</a>
* <a href="https://pypi.org/project/bcrypt/">Bcrypt</a>
* <a href="https://pypi.org/project/colorama/">Colorama</a>
* <a href="https://pypi.org/project/termcolor/">Termcolor</a>
* <a href="https://pypi.org/project/pyperclip/">Pyperclip</a>

### Installation and Usage
```shell
$ pip3 install passwordmanager
$ # path/to/python path/to/passman
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
# note that the python versions in this example might not be the version you're using, adjust accordingly
# the following works for most MacOS users:
$ PATH_TO_PYTHON = "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages"
$ echo "alias passman='python3 $PATH_TO_PYTHON'" > ~/.bashrc
# the following works for most Windows 10 users:
$ PATH_TO_PYTHON = "/c/Program Files (x86)/Python36-32/Lib/site-packages/passman/__main__.py"
$ echo "alias passman='python3 $PATH_TO_PYTHON'" > /.bashrc
```

\* This package was uploaded using <a href="https://anweshadas.in/how-to-upload-a-package-in-pypi-using-twine/">twine</a>:
```shell
$ python3 setup.py sdist
$ twine upload dist/*
```


**TODO:**
* Separate main menu functions into own module
* Update/delete passwords from database

**Author:**  
Sean Pierce Sumler

**License:**  
MIT, use at your own risk

For questions and comments please <a href="https://github.com/seanpierce/passman/issues/new">raise an issue</a>. <a href="https://github.com/seanpierce/passman/compare">Pull requests</a> always welcome, too. Thanks!
