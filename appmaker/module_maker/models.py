# -*- coding: utf-8 -*-
import datetime
from flask import url_for
from flaskstarter import db
from mongoengine import ReferenceField


class ObjectFields(db.Document):
    name = db.StringField(max_length=100)
    label = db.StringField(max_length=100)
    help_text = db.StringField(max_length=100)
    placeholder = db.StringField(max_length=100)
    type = db.StringField(max_length=100)
    read_only = db.BooleanField(default=False)
    visible = db.BooleanField(default=False)
    is_relation_column = db.BooleanField(default=False)
    relation = db.StringField(max_length=100)
    relation_column_name = db.StringField(max_length=100)
    index = db.StringField(max_length=100)
    pid = db.StringField(max_length=100)

class BussinessObject(db.Document):
    api_name = db.StringField(max_length=100)
    name = db.StringField(max_length=100)
    object_id = db.StringField(max_length=100)
    order = db.IntField()
    description = db.StringField(max_length=100)
    create_date = db.DateTimeField(default=datetime.datetime.now)


class Module(db.Document):
    api_name = db.StringField(max_length=100)
    name = db.StringField(max_length=100)
    description = db.StringField(max_length=100)
    create_date = db.DateTimeField(default=datetime.datetime.now)
    bussiness_objects = db.ListField(ReferenceField(BussinessObject))

