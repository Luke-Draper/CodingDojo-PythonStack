from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'JimmyKnows'

@app.route('/')
def default():
	return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
	name = request.form['name']
	location = request.form['location']
	favorite_language = request.form['favorite_language']
	comment = request.form['comment']
	result_data = {'name':name, 'location':location, 'favorite_language':favorite_language, 'comment':comment, }
	return render_template("result.html", results=result_data)

@app.route('/danger')
def danger():
	print("a user tried to visit /danger. we have redirected the user to /")
	return redirect('/')

@app.route('/reset_session')
def reset():
	session.clear()
	return redirect('/')

@app.route('/guess', methods=['POST'])
def guess():
	session['guess'] = int(request.form['guess'])
	return redirect('/')


if __name__=="__main__":
	app.run(debug=True)