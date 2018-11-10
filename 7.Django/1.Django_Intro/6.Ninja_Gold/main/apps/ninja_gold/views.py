from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
	if 'current_gold' not in request.session:
		request.session['current_gold'] = 0
	if 'history' not in request.session:
		new_array = []
		request.session['history'] = new_array
	return render(request,"ninja_gold/index.html")


def find_gold(request):
	if request.method == "POST":
		update_session_gold(request,request.POST['location'])
		return redirect("/")
	else:
		return redirect("/")

def update_session_gold(request,location):
	gold_earned = 0
	if location == "farm":
		gold_earned = random.randrange(10,21)
	if location == "cave":
		gold_earned = random.randrange(5,11)
	if location == "house":
		gold_earned = random.randrange(2,6)
	if location == "casino":
		gold_earned = random.randrange(-50,51)
	request.session['current_gold'] += gold_earned
	history = request.session['history']
	history.append({"location":location, "gold_earned":gold_earned})
	request.session['history'] = history


def reset(request):
	del request.session["history"]
	del request.session["current_gold"]
	return redirect("/")


