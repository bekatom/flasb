# -*- coding: utf-8 -*-
from flask import request, redirect, render_template, url_for, session, escape, jsonify, g
from flaskstarter import app
from flask.ext.login import login_required ,current_user


@app.route('/user', methods=['POST', 'GET'])
@app.route('/user')
@login_required
def main_user():
    return render_template('modules/user/index.html')
