# -*- coding: utf-8 -*-
from flask import request, redirect, render_template, url_for, session, escape, jsonify, g
from flaskstarter import app
from flask.ext.login import login_required ,current_user


@app.route('/module_name', methods=['POST', 'GET'])
@app.route('/module_name')
@login_required
def main_module_name():
    return render_template('modules/module_name/index.html')
