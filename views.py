# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect, render_template, url_for,session, escape,jsonify,g
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form
from flaskstarter import  app




#### ERROR HANDLER #########
@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'),404



@app.route('/',methods=['POST','GET'])
@app.route('/')
def main():
	if g.sijax.is_sijax_request:
		call_test_callbacks(g)
		return g.sijax.process_request()
	return render_template('index.html')


@app.route('/contact',methods=['POST','GET'])
@app.route('/contact')
def contact():
	if request.method =='POST':
		message = 'This is post message'
		return render_template('contact.html',message=message)
	else:
		return render_template('contact.html')


@app.route('/about')
def about():
	return render_template('about.html')



@app.route('/login',methods=['POST','GET'])
def login():
	if request.method =='POST':
		email = request.form['email']
		password = request.form['password']

		""" 
			From mongo database
			#user = User.objects.get(email = email)
		"""
		
		if email == 'beka@vobi.ge' and password =='qwerty':
			session['is_auth'] = True
			session['email'] = email
			return render_template('index.html',session=session)
		else:
			return render_template('login.html',message="Email or password is incorrect, try again")    
	else:
		return render_template('login.html')


@app.route('/registration',methods=['POST','GET'])
def registration():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']

		"""
		Registration in Mongo database

		user = User(identification = identification,
					email= email,
					password = password
					)
		user.save()

		"""
		return  redirect(url_for('login',message="????? ?????????? ??????? ??????????? "
												 "????? ??????? ???????????"))
	else:
		return  render_template('registration.html')


## SIJAX METHODS ############
def hello_handler(obj_response, hello_from, hello_to):
	obj_response.alert('Hello from %s to %s' % (hello_from, hello_to))
	obj_response.css('a', 'color', 'green')

def goodbye_handler(obj_response):
	obj_response.alert('Goodbye, whoever you are.')
	obj_response.css('a', 'color', 'red')




def call_test_callbacks(g):
	g.sijax.register_callback('say_hello', hello_handler)
	g.sijax.register_callback('say_goodbye', goodbye_handler)


## LOGOUT
@app.route('/logout')
def logout():
	#remove username from session
	session.pop('is_auth',None)
	session.pop('email',None)
	return  redirect(url_for('main'))