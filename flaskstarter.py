# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext import login
from flask.ext.login import LoginManager

import os


app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object('config.ProductionConfig')
login_manager = LoginManager()
login_manager.init_app(app)


db = MongoEngine(app)

from views import *
from apps.auth.views import *

login_manager.login_view = 'login'

if __name__ == '__main__':
    app.run(port=5000, host="localhost")
