# -*- coding: utf-8 -*-
__author__ = 'Beka'
from flask import Blueprint, request, redirect, render_template, url_for, session, escape, jsonify, g, flash
from flask.ext.login import login_user, logout_user, current_user, login_required
from models import User
from mongoengine.queryset import DoesNotExist
from flaskstarter import app, login_manager
import requests


def sendletter(user, email, password):
    subject = u"თქვენ წარმათებით გარეთ რეგისტრაცია VOBI Cloud სერვისზე"
    body = u"ავტორიზაციისთვის გამოიყენეთ შემდეგი პარამეტრები %s , პაროლი %s " % (email, password)
    emailto = email
    return requests.post(
        "https://api.mailgun.net/v2/sandboxc3eeb6601b344b2f94eea98103573f69.mailgun.org/messages",
        auth=("api", "key-930hiya4r1jeo82zqjo8m8m2ptm08gj3"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxc3eeb6601b344b2f94eea98103573f69.mailgun.org>",
              "to": "beka <beka@vobi.ge>",
              "subject": subject,
              "text": body})


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
                flash(u"Not valid email")
                return redirect(url_for('signup'))
            if request.form['password'] != request.form['rpassword']:
                flash(u"პაროლი არ ემთხვევა , გთხოვთ ცადოთ თავიდან")
                return redirect(url_for('signup'))

            user.email = request.form['email']
            user.password = request.form['password']
            user.theme = 'yeti' # default teheme after registratiosn
            user.app_name = 'FLASB'
            # user.Applicant = request.form['Email']
            user.save()
            sendletter(user, user.email, user.password)  # send letter to email
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


