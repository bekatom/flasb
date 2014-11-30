# -*- coding: utf-8 -*-
__author__ = 'Beka'
import datetime
from flaskstarter import db
from mongoengine import EmbeddedDocumentField, EmbeddedDocument, ReferenceField
from mongoengine.queryset import DoesNotExist
from appmaker.module_maker.models import Module, BussinessObject


class User(db.Document):
    email = db.StringField(max_length=100)
    fullname = db.StringField(max_length=100)
    name = db.StringField(max_length=100)
    surname = db.StringField(max_length=100)
    password = db.StringField(max_length=100)
    create_date = db.DateTimeField(default=datetime.datetime.now)
    is_admin = db.BooleanField(default=False)
    is_stoped = db.BooleanField(default=False)
    theme = db.StringField(max_length=100)
    app_name = db.StringField(max_length=100)
    modules = db.ListField(ReferenceField(Module))
    module_objects = db.ListField(ReferenceField(BussinessObject))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(str(self.id))

    def is_super_user(self):
        return self.is_admin

    def get_email(self):
        return self.email

    def get_theme(self):
        return self.theme

    def get_fullname(self):
        return self.fullname

    # def __unicode__(self):
    #    return self.identification

    def get_user(self, email, password):
        try:
            user = User.objects.get(email=email, password=password)
            return user
        except DoesNotExist:
            return None

    def __repr__(self):
        return '<User %r>' % (str(self.id))
