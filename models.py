from collections import OrderedDict
import datetime
import sys

class BaseModel(Model):
    class Meta:
        database = db

class Password(BaseModel):
    application = CharField(max_length = 255)
    login = CharField(max_length = 255)
    password = CharField(max_length = 255)
    notes = TextField(null = False)
    modified_at = DateTimeField(default = datetime.datetime.now)
