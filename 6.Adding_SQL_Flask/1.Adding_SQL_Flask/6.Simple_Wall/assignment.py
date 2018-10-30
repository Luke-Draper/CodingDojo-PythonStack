from flask import Flask, render_template, request, redirect, session, flash
import re
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'JimmyKnows'
bcrypt = Bcrypt(app)

# email
# first_name
# last_name
# password
# confirm_password
def validation_form(form):
	valid = True
	if not validation_fields_not_blank(form):
		valid = False
	else:
		if not validation_email(form):
			valid = False
		if not validation_name_no_digits(form):
			valid = False
		if not validation_password(form):
			valid = False
	return valid

def validation_login(form):
	valid = True
	if not validation_fields_not_blank(form):
		valid = False
	else:
		if not validation_email(form):
			valid = False
		if not validation_login_password(form):
			valid = False
	return valid

# All fields are required and must not be blank
def validation_fields_not_blank(form):
	valid = True
	for key in form:
		if len(form[key]) < 1:
			valid = False
			flash("All fields are required", "danger")
			break
	return valid

# Email should be a valid email
# This function is based off of this webpages regex
# https://www.pythoncentral.io/how-to-validate-an-email-address-using-python/
def validation_email(form):
	valid = False
	if len(form['email']) > 7:
		if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',form['email']) != None:
			valid = True
		else:
			flash("Email is invalid", "danger")
	else:
		flash("Email is invalid", "danger")
	return valid

# First and Last Name cannot contain any numbers
def validation_name_no_digits(form):
	valid = True
	if not any(char.isdigit() for char in form['first_name']) < 1:
		valid = False
		flash("First name cannot contain numbers", "danger")
	if not any(char.isdigit() for char in form['last_name']) < 1:
		valid = False
		flash("Last name cannot contain numbers", "danger")
	return valid

# Password should be more than 8 characters
# Password and Password Confirmation should match and have at least 1 lomercase letter 1 uppercase letter and 1 numeric value
def validation_password(form):
	valid = False
	if form['password'] == form['confirm_password']:
		if len(form['password'])>=8:
			if any(char.isdigit() for char in form['password']) > 0:
				if any(char.islower() for char in form['password']) > 0:
					if any(char.isupper() for char in form['password']) > 0:
						valid = True
					else:
						flash("Password must contain at least 1 uppercase character, 1 uppercase character, and 1 digit", "danger")
				else:
					flash("Password must contain at least 1 uppercase character, 1 uppercase character, and 1 digit", "danger")
			else:
				flash("Password must contain at least 1 uppercase character, 1 uppercase character, and 1 digit", "danger")
		else:
			flash("Password must be longer than 8 characters", "danger")
	else:
		flash("Passwords must match", "danger")
	return valid

def validation_login_password(form):
	valid = False
	user = get_user_by_email(form['email'])
	if bcrypt.check_password_hash(user['password_hash'], form['password']):
		valid = True
	return valid

@app.route('/')
def default():
	if 'user_id' not in session:
		session['user_id'] = None
	if session['user_id'] != None:
		if len(get_user_by_id(session['user_id']))>0:
			return redirect("/success")
	return render_template("index.html")

@app.route('/success')
def success():
	return render_template("success.html", user=get_user_by_id(session['user_id']), other_users=get_user_except_id(session['user_id']), in_messages=get_messages_to_user(session['user_id']))

@app.route('/register', methods=['POST'])
def register():
	if validation_form(request.form):
		flash("Thanks for submitting your information", "success")
		insert_user(request.form)
		session['user_id'] = get_user_by_email(request.form['email'])["user_id"]
	return redirect('/')

@app.route('/login', methods=['POST'])
def login():
	if validation_login(request.form):
		session['user_id'] = get_user_by_email(request.form['email'])["user_id"]
	return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
	if session['user_id'] != None:
		session['user_id'] = None
	return redirect('/')

@app.route('/send', methods=['POST'])
def send():
	if session['user_id'] != None:
		message = {
			'content':request.form["content"],
			'to_id':request.form["to_id"],
			'from_id':session["user_id"]
		}
		insert_message(message)
		flash("Message sent succesfully", "success")
	return redirect('/')

# Hi12345678

def get_user_by_id(user_id):
	mysql = connectToMySQL('basic_wall')
	return mysql.query_db("SELECT users.user_id, users.first_name, users.last_name, users.email, users.password_hash, created_at, updated_at FROM users WHERE user_id = "+str(user_id)+";")[0]

def get_user_except_id(user_id):
	mysql = connectToMySQL('basic_wall')
	return mysql.query_db("SELECT users.user_id, users.first_name, users.last_name, users.email, users.password_hash, created_at, updated_at FROM users WHERE user_id != "+str(user_id)+";")

def get_user_by_email(email):
	mysql = connectToMySQL('basic_wall')
	return mysql.query_db("SELECT users.user_id, users.first_name, users.last_name, users.email, users.password_hash, created_at, updated_at FROM users WHERE email = '"+email+"';")[0]

def insert_user(user):
	password_hash = bcrypt.generate_password_hash(user['password']).decode("utf-8")
	mysql = connectToMySQL('basic_wall')
	return mysql.query_db("INSERT INTO users (first_name, last_name, email, password_hash, created_at, updated_at) VALUES ('"+user['first_name']+"','"+user['last_name']+"','"+user['email']+"','"+password_hash+"', CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());")

def get_messages_to_user(user_id):
	mysql = connectToMySQL('basic_wall')
	return mysql.query_db("SELECT message.*, to_user.*, from_user.* FROM messages message JOIN users to_user ON to_user.user_id = message.to_id JOIN users from_user ON from_user.user_id = message.from_id WHERE message.to_id = "+str(user_id)+";")

def insert_message(message):
	mysql = connectToMySQL('basic_wall')
	return mysql.query_db("INSERT INTO messages (content, to_id, from_id, created_at, updated_at) VALUES ('"+message['content']+"',"+str(message['to_id'])+","+str(message['from_id'])+", CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());")

if __name__=="__main__":
	app.run(debug=True)