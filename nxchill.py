from flask import flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import owner as o
app = Flask(__name__)

@app.route('/')
def home():
	render_template('Welcome.html')
	pass

@app.route('/register')
def register():
	render_template('Register.html')
	pass 
@app.route('/Find')
def Find():
	render_template('find.hml')
@app.route('/registered', methods = ['POST'])
def registered():
	email = request.form['Email']
	scr = request.form['scr']
	ascr = request.form['ascr']
	msg = request.form['msg']
	o.owner(email,scr,ascr,msg)
	o.register()
	return home()