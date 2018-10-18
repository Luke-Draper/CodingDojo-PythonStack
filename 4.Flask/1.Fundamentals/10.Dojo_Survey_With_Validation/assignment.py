from flask import Flask, render_template, request, redirect, session, flash
import random
app = Flask(__name__)
app.secret_key = 'JimmyKnows'

# Add validations to check that the name and comment fields are not blank (display appropriate validation errors)
# Add validations to check that the comment is no more than 120 characters (display appropriate validation errors)

@app.route('/')
def default():
	return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
	error = False
	if len(request.form['name']) < 1:
		error = True
		flash("Name is blank")
	if len(request.form['comment']) < 1:
		error = True
		flash("Comment is blank")
	if len(request.form['comment']) > 120:
		error = True
		flash("Comment is too long")
	if not error:
		session['result_data'] = {'name':request.form['name'], 'location':request.form['location'], 'favorite_language':request.form['favorite_language'], 'comment':request.form['comment']}
		return redirect('/result')
	return redirect('/')

@app.route('/result')
def result():
	return render_template("result.html", results=session['result_data'])

@app.route('/danger')
def danger():
	print("a user tried to visit /danger. we have redirected the user to /")
	return redirect('/')

if __name__=="__main__":
	app.run(debug=True)