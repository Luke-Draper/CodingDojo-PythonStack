from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default():
	return render_template("index.html", x=8, y=8)

@app.route('/<numx>/<numy>')
def number(numx, numy):
	numx = int(numx)
	numy = int(numy)
	return render_template("index.html", x=numx, y=numy)

if __name__=="__main__":
	app.run(debug=True)