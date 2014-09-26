# -*- coding: utf-8 -*-
from flask import request, redirect, render_template, url_for, session, escape, jsonify, g
from flaskstarter import app
from flask.ext.login import login_required



# ### ERROR HANDLER #########
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/', methods=['POST', 'GET'])
@app.route('/')
@login_required
def main():
    return render_template('index.html')


