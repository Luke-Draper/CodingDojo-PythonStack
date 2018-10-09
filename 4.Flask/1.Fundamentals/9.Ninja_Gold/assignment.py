from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'JimmyKnows'

@app.route('/')
def default():
	if 'current_gold' not in session:
		session['current_gold'] = 0
	if 'history' not in session:
		session['history'] = []
	return render_template("index.html")

@app.route('/find_gold', methods=['POST'])
def result():
	update_session_gold(request.form['location'])
	return redirect('/')

def update_session_gold(location):
	gold_earned = 0
	if location == "farm":
		gold_earned = random.randrange(10,21)
	if location == "cave":
		gold_earned = random.randrange(5,11)
	if location == "house":
		gold_earned = random.randrange(2,6)
	if location == "casino":
		gold_earned = random.randrange(-50,51)
	session['current_gold'] += gold_earned
	session['history'].append({"location":location, "gold_earned":gold_earned})

@app.route('/reset_session')
def reset():
	session.clear()
	return redirect('/')

if __name__=="__main__":
	app.run(debug=True)