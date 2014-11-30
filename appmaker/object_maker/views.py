# -*- coding: utf-8 -*-
from flask import request, redirect, render_template, url_for, session, escape, jsonify, g
from flaskstarter import app
from flask.ext.login import login_required, current_user
from apps.auth.models import User
from appmaker.module_maker.models import BussinessObject, Module




@app.route('/appmaker/objectmaker', methods=['POST', 'GET'])
@login_required
def objectmaker():
    try:
        if request.method == 'POST':
            module_id = request.form['module']
            module = Module.objects.get(pk=module_id)
            obj = BussinessObject()
            obj.api_name = request.form['api-name']
            obj.name = request.form['name']
            obj.description = request.form['description']
            obj.save()
            module.bussiness_objects.append(obj)
            module.save()

    except Exception, e:
        print e

    modules = current_user.modules
    return render_template('appmaker/objectmaker/index.html',modules = modules)


@app.route('/appmaker/obj/delete/<module_id>/<obj_id>', methods=['POST', 'GET'])
@login_required
def obj_delete(module_id=None, obj_id=None):
    try:
        if obj_id is not None:
            obj = BussinessObject.objects.get(pk=obj_id)
            obj.delete()
            return redirect('/appmaker/module/%s' %module_id)

    except Exception, e:
        print e
