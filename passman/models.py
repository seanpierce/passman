import datetime
import sys
from collections import OrderedDict

from peewee import *

db = SqliteDatabase('passman.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(max_length = 125, unique = True)
    password_hash = CharField(max_length = 255)

class Password(BaseModel):
    user = ForeignKeyField(User, backref='passwords')
    application = CharField(max_length = 255)
    login = CharField(max_length = 255)
    password = CharField(max_length = 255)
    notes = TextField(null = False)
    modified_at = DateTimeField(default = datetime.datetime.now)
