# -*- coding: utf-8 -*-
from flask import request, redirect, render_template, url_for, session, escape, jsonify, g
from flaskstarter import app
from flask.ext.login import login_required ,current_user
from config import BOOTSTRAP_THEMS
from apps.auth.models import User
import os
from appmaker.config import MODULES_FOLDER

dirs = [x for x in os.listdir(MODULES_FOLDER) if os.path.isdir(os.path.join(MODULES_FOLDER, x))]
mlist = []
for m in dirs:
    itm = 'modules.%s.views' % m
    mlist.append(itm)


modules = map(__import__, mlist)

# ### ERROR HANDLER #########
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/', methods=['POST', 'GET'])
@app.route('/')
@login_required
def main():
    return render_template('index.html')


@app.route('/settings', methods=['POST', 'GET'])
@login_required
def settings():
    if request.method == 'POST':
        theme = request.form['theme']
        app_name = request.form['app-name']
        if current_user.is_authenticated():
            user = User.objects.get(pk=current_user.id)
            user.theme = theme
            user.app_name = app_name
            user.save()
            return redirect(url_for('settings'))

    return render_template('settings.html',BOOTSTRAP_THEMS=BOOTSTRAP_THEMS)