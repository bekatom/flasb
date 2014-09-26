# -*- coding: utf-8 -*-
__author__ = 'Beka'
import datetime
from flaskstarter import db
from mongoengine import EmbeddedDocumentField,EmbeddedDocument


class CompanyDetails(EmbeddedDocument):
    identification = db.StringField(max_length=100)
    fav_id = db.StringField(max_length=150)
    comments = db.ListField(db.StringField(max_length=150))
    color = db.StringField(max_length=100)
    create_date = db.DateTimeField(default=datetime.datetime.now)

class User(db.Document):
    email = db.StringField(max_length=100)
    fullname = db.StringField(max_length=100)
    name = db.StringField(max_length=100)
    surname = db.StringField(max_length=100)
    password = db.StringField(max_length=100)
    create_date = db.DateTimeField(default=datetime.datetime.now)
    is_admin = db.BooleanField(default=False)
    is_stoped = db.BooleanField(default=False)
    companies = db.ListField(EmbeddedDocumentField(CompanyDetails))

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

    def get_fullname(self):
        return self.fullname

    #def __unicode__(self):
    #    return self.identification

    def __repr__(self):
        return '<User %r>' % (str(self.id))
