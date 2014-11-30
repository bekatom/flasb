# -*- coding: utf-8 -*-
from flask import request, redirect, render_template, url_for, session, escape, jsonify, g
from flaskstarter import app
from flask.ext.login import login_required, current_user
from apps.auth.models import User
from construct import exec_modul_constructor
import shutil
from appmaker.config import MODULES_FOLDER, TEMPLATE_DIR
from appmaker.module_maker.models import BussinessObject, Module

@app.route('/appmaker/modulemaker', methods=['POST', 'GET'])
@login_required
def modulemaker():
    try:
        if request.method == 'POST':
            module = Module()
            module.api_name = request.form['api-name']
            module.name = request.form['name']
            module.description = request.form['description']
            module.save()
            user = User.objects.get(pk=current_user.id)
            user.modules.append(module)
            user.save()
            exec_modul_constructor(module.api_name)
    except Exception, e:
        print e

    return render_template('appmaker/modulemaker/index.html')


@app.route('/appmaker/deletemodule/<module_id>', methods=['POST', 'GET'])
@login_required
def delete_module(module_id=None):
    module = Module()
    try:
        if module_id is not None:
            module = Module.objects.get(pk=module_id)
            api_name = module.api_name
            User.objects(pk=current_user.id).update(pull__modules=module)
            shutil.rmtree(MODULES_FOLDER+'/'+api_name)
            shutil.rmtree(TEMPLATE_DIR+'/'+api_name)
            return redirect('/appmaker')
    except Exception, e:
        print e
