from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = 'JimmyKnows'

# Create a simple registration page with the following fields:
# email
# first_name
# last_name
# birth_date
# password
# confirm_password

# Here are the validations you must include:
def validation_form(form):
	valid = True
	if not validation_fields_not_blank(form):
		valid = False
	else:
		if not validation_email(form):
			valid = False
		if not validation_name_no_digits(form):
			valid = False
		if not validation_birth_date(form):
			valid = False
		if not validation_password(form):
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
	print(valid)
	return valid

# Birth Date a valid date and must be from the past
def validation_birth_date(form):
	valid = False
	if len(form['birth_date']) == 10:
		if re.match("\d\d\d\d-\d\d-\d\d", form['birth_date']) != None:
			year = int(form['birth_date'][:4])
			current_year = 2018
			if year < current_year:
				valid = True
			elif year == current_year:
				month = int(form['birth_date'][5:7])
				current_month = 10
				if month < current_month:
					valid = True
				elif month == current_month:
					day = int(form['birth_date'][9:])
					current_day = 17
					if day <= current_day:
						valid = True
					else:
						flash("Birth date must be in the past", "danger")
				else:
					flash("Birth date must be in the past", "danger")
			else:
				flash("Birth date must be in the past", "danger")
		else:
			flash("Birth date format is invalid", "danger")
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

# When the form is submitted, make sure the user submits appropriate information.
# If the user did not submit appropriate information, return the error(s) above the form that asks the user to correct the information. 

# For this, you will need to use flash messages at the very least. You may have to take this one step further and add
# categories to the flash messages. You can learn that from the flask doc: http://flask.pocoo.org/docs/1.0/patterns/flashing/#flashing-with-categories

# If the form with all the information is submitted properly, simply have it say a message "Thanks for submitting your information."

@app.route('/')
def default():
	return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
	if validation_form(request.form):
		flash("Thanks for submitting your information", "success")
	return redirect('/')

# Hi12345678

if __name__=="__main__":
	app.run(debug=True)