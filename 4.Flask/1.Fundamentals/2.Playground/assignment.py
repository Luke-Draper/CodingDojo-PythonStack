from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def default():
	return render_template("index.html", number=3, color="blue")

@app.route('/play/<num>')
def number(num):
	num = int(num)
	return render_template("index.html", number=num, color="blue")

@app.route('/play/<num>/<col>')
def color(num, col):
	num = int(num)
	col = str(col)
	return render_template("index.html", number=num, color=col)

if __name__=="__main__":
	app.run(debug=True)