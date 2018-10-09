from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'JimmyKnows'

@app.route('/')
def default():
	if 'count' in session:
		session['count'] += 1
	else:
		session['count'] = 1
	return render_template("index.html")

@app.route('/destroy_session')
def destroy():
	session.clear()
	return redirect('/')

@app.route('/add/<num>')
def add(num):
	session['count'] += (int(num)-1)
	return redirect('/')

@app.route('/reset_session')
def reset():
	session['count'] = 0
	return redirect('/')

if __name__=="__main__":
	app.run(debug=True)