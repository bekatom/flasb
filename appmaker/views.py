# -*- coding: utf-8 -*-
from flask import request, redirect, render_template, url_for, session, escape, jsonify, g
from flaskstarter import app
from flask.ext.login import login_required, current_user
from apps.auth.models import User


from module_maker.views import *
from object_maker.views import *



@app.route('/appmaker', methods=['POST', 'GET'])
@login_required
def appmaker():
    return render_template('appmaker/index.html')


@app.route('/appmaker/module/<module_id>', methods=['POST', 'GET'])
@login_required
def module_page(module_id=None):
    if module_id is not None:
        module = Module.objects.get(pk=module_id)
        return render_template('appmaker/module.html', module=module)


@app.route('/appmaker/module/obj/<obj_id>', methods=['POST','GET'])
@login_required
def bussiness_object(obj_id=None):
    if obj_id is not None:
        obj = BussinessObject.objects.get(pk=obj_id)
        return render_template('appmaker/object.html', obj=obj)
