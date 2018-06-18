# PassMan
Passman is a Python-based password management application. Data is managed using Peewee and stored in a Sqlite3 database.

### Dependencies
* Python3
  * Check version using `$ python --version`
  * <a href="https://www.python.org/downloads/release/python-365/">Upgrading to Python3</a>
* PeeWee
  * `pip3 install peewee`

### Installation and Usage
* ```shell
  $ git clone https://github.com/seanpierce/passman
  $ cd passman
  $ chmod +x passman.py
  $ ./passman.py
  ```

**Notes:**
* It's helpful to alias "python" and "pip" to point towards the "python3" and "pip3" commands respectively
* ```shell
  $ echo "alias python=python3" > ~/.bashrc
  $ echo "alias pip=pip3" > ~/.bashrc
  $ # for zsh users, replace .bachrc with .zshrc
  ```

**TODO:**
* Authenticate user with encrypted master password
* Associate stored passwords with the current user
* Implement multi-line input for handling all fields for a password model
