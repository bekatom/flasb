# -*- coding: utf-8 -*-
from flask import request, redirect, render_template, url_for, session, escape, jsonify, g
from flaskstarter import app
from flask.ext.login import login_required, current_user
from apps.auth.models import User


from module_maker.views import *




@app.route('/appmaker', methods=['POST', 'GET'])
@login_required
def appmaker():
    return render_template('appmaker/index.html')




