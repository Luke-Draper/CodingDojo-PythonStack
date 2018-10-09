from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'JimmyKnows'

@app.route('/')
def default():
	if 'number' not in session:
		session['number'] = random.randrange(1,101)
	template = "index.html"
	if 'guess' in session:
		if session['guess'] > session['number']:
			template = "great.html"
		elif session['guess'] < session['number']:
			template = "less.html"
		else:
			template = "success.html"
	return render_template(template)

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