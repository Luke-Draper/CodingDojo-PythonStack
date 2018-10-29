from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'JimmyKnows'

@app.route('/')
def default():
	return render_template("index.html")

@app.route('/success')
def success():
	return render_template("success.html", emails=get_emails())

@app.route('/submit', methods=['POST'])
def submit():
	if validate_email(request.form["email"]):
		insert_email(request.form["email"])
		return redirect('/success')
	else:
		return redirect('/')

def get_emails():
	mysql = connectToMySQL('email_validation')
	return mysql.query_db("SELECT emails.email, emails.created_at FROM emails ORDER BY emails.created_at DESC;")

def validate_email(email):
	email = email.lower()
	valid = False
	if len(email) > 7:
		if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',email) != None:
			valid = True
		else:
			flash("Email is invalid", "danger")
	else:
		flash("Email is invalid", "danger")
	return valid

def insert_email(email):
	email = email.lower()
	mysql = connectToMySQL('email_validation')
	return mysql.query_db("INSERT INTO emails (email, created_at) VALUES ('"+email+"', CURRENT_TIMESTAMP());")

if __name__=="__main__":
	app.run(debug=True)