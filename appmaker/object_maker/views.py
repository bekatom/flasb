# -*- coding: utf-8 -*-
from flask import request, redirect, render_template, url_for, session, escape, jsonify, g
from flaskstarter import app
from flask.ext.login import login_required, current_user
from apps.auth.models import User
from models import Module, ModuleObjects

@app.route('/appmaker/object', methods=['POST', 'GET'])
@login_required
def modulemaker():
    try:
        if request.method == 'POST':
            obj = ModuleObjects()
            obj.api_name = request.form['api-name']
            obj.name = request.form['name']
            obj.description = request.form['description']
            user = User.objects.get(pk=current_user.id)
            user.modules.append(obj)
            user.save()
    except Exception, e:
        print e

    return render_template('appmaker/modulemaker/index.html')
