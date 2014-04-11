# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.mongoengine import MongoEngine
import os
import flask_sijax

app = Flask(__name__)
app.config.from_object('config.ProductionConfigHome')

path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'

flask_sijax.Sijax(app)

db = MongoEngine(app)

from views import *


if __name__ == '__main__':
    app.run()
