# -*- coding: utf-8 -*-
import datetime
from flask import url_for
from flaskstarter import db
from mongoengine import EmbeddedDocumentField, EmbeddedDocument

class Module(EmbeddedDocument):
    api_name = db.StringField(max_length=100)
    name = db.StringField(max_length=100)
    description = db.StringField(max_length=100)
    create_date = db.DateTimeField(default=datetime.datetime.now)

class Objects(EmbeddedDocument):
    module_api_name = db.StringField(max_length=100)
    api_name = db.StringField(max_length=100)
    name = db.StringField(max_length=100)
    object_id = db.StringField(max_length=100)
    order = db.IntField()
    description = db.StringField(max_length=100)
    create_date = db.DateTimeField(default=datetime.datetime.now)