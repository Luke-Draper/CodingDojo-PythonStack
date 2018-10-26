from flask import Flask, render_template, request, redirect, session
import random
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'JimmyKnows'

@app.route('/')
def default():
	return render_template("index.html", customers=get_customers())

def get_customers():
	mysql = connectToMySQL('leads_clients')
	return mysql.query_db("SELECT customers.name, customers.lead FROM customers;")

# # SELECT first_name, last_name, occupation FROM friends;

# @app.route('/add_friend', methods=['POST'])
# def result():
# 	if validate_friend(request.form):
# 		add_friend(request.form)
# 	return redirect('/')

# def validate_friend(friend_dict):
# 	output = True
# 	if len(friend_dict['first_name']) < 1:
# 		output = False
# 	if len(friend_dict['last_name']) < 1:
# 		output = False
# 	if len(friend_dict['occupation']) < 1:
# 		output = False
# 	return output

# def add_friend(friend_dict):
# 	mysql = connectToMySQL('c_r_friends')
# 	return mysql.query_db("INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES ('"+ friend_dict['first_name'] +"', '"+ friend_dict['last_name'] +"', '"+ friend_dict['occupation'] +"', CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());")

# # INSERT INTO customers (name, lead, occupation, created_at, updated_at) VALUES ("Zaphod", 6);

if __name__=="__main__":
	app.run(debug=True)