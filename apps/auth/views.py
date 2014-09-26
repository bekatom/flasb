# -*- coding: utf-8 -*-
__author__ = 'Beka'
from flask import Blueprint, request, redirect, render_template, url_for, session, escape, jsonify, g, flash
from flask.ext.login import login_user, logout_user, current_user, login_required
from models import User
from mongoengine.queryset import DoesNotExist
from flaskstarter import app, login_manager




@login_manager.user_loader
def load_user(id):
    return User.objects.get(pk=id)



@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        u = User()
        user = u.get_user(email, password)
        if user is not None:
            login_user(user)  # this is flask login
            return redirect(url_for('main'))
        else:
            return render_template('apps/auth/login.html', message="Email or password is incorrect, try again")

    else:
        return render_template('apps/auth/login.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    user = User()
    if request.method == 'POST':
        try:
            if request.form['email'] != request.form['remail']:
                flash(u"ელ-ფოსტა არავალიდურია")
                return redirect(url_for('signup'))
            if request.form['password'] != request.form['rpassword']:
                flash(u"პაროლი არ ემთხვევა , გთხოვთ ცადოთ თავიდან")
                return redirect(url_for('signup'))

            user.email = request.form['email']
            user.password = request.form['password']
            # user.Applicant = request.form['Email']
            user.save()
            flash(u"თქვენ წარმატებით გაიარეთ რეგსიტრაცია, გთხოვთ იხილოთ თქვენი ელ-ფოსტა")
            return redirect(url_for('main'))
        except Exception, e:
            return "<h1> ERROR ON PAGE PlEASE TRY AGAIN LATER</h1>"

    else:
        return render_template('apps/auth/signup.html')


# LOGOUT
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main'))


