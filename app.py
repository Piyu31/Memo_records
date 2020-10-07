from flask import Flask,render_template,redirect,request,session,flash,url_for,g
import datetime
import sys
import random
import time

import json

import database_orc

app = Flask(__name__)

#GCD (Good Coding Practice)
app.secret_key="478006hr478hvdeygsy"

@app.route("/")
def index():
	
#getting memorecord data
	memo_records= database_orc.get_memorecords()
	memorecordlist =[]
	for r in memo_records:
		memorecordlist.append(r)
		
		
	return render_template('base.html', memolist = memorecordlist)





@app.route("/memo", methods=['POST'])
def update_memorecordsdb():
	#for memorecords collection data	
	newdata = {}
	com_name = request.form['com_name']
	date = request.form['date']
	to = request.form['to']
	f_rom = request.form['f_rom']
	subject = request.form['subject']
	text_body = request.form['text_body']
	list_data = request.form['list_data']
	name = request.form['name']
	email = request.form['email']
	#send data to db
	newdata["com_name"] = com_name
	newdata["date"] = date
	newdata["to"] = to
	newdata["f_rom"] = f_rom
	newdata["subject"] = subject
	newdata["text_body"] = text_body
	newdata['list_data'] = list_data
	newdata["name"] = name
	newdata["email"] = email
	print (newdata)
	database_orc.save_memorecords(newdata)
	return redirect(url_for('index'))

