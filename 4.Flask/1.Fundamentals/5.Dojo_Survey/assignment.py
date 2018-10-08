from flask import Flask, render_template, request, redirect
app = Flask(__name__)

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


if __name__=="__main__":
	app.run(debug=True)