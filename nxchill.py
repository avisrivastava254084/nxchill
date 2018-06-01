import json
import csv
import ast
from time import sleep
from Owner import Owner
from Tenant import Tenant
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
fileName = "Owners.csv"
app = Flask(__name__)
@app.route('/')
def home():
	return render_template('Welcome.html')
	pass
@app.route('/Register')
def register():
	return render_template('Register.html')
	pass
@app.route('/Find')
def Find():
	return render_template('Find.html')
@app.route('/registered', methods = ['POST'])
def registered():
	email = request.form['Email']
	scr = request.form['scr']
	ascr = request.form['ascr']
	msg = request.form['msg']
	obOwner = Owner(email,scr,ascr,msg)
	obOwner.advertise()
	print("Registered!")
	sleep(2)
	return render_template('Welcome.html')
@app.route('/found', methods = ['POST'])
def found():
	checkVariable = 0
	matchList = []
	screens = request.form['rscr']
	with open(fileName, 'rb') as csv_reader:
		reader = csv.reader(csv_reader)
		for row in reader:
			currDict = ast.literal_eval(row[0])
			if(screens <= currDict["availableScreens"]):
				checkVariable = 1
				matchList.append(currDict)
	if(len(matchList) >= 1):
		jsonList = json.dumps(matchList)
		return jsonList
	return "No screens available"

if __name__ == "__main__":
	app.run()