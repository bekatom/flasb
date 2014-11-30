# -*- coding: utf-8 -*-
from flask import request, redirect, render_template, url_for, session, escape, jsonify, g
from flaskstarter import app
from flask.ext.login import login_required ,current_user


@app.route('/users', methods=['POST', 'GET'])
@app.route('/users')
@login_required
def main_users():
    return render_template('modules/users/index.html')
