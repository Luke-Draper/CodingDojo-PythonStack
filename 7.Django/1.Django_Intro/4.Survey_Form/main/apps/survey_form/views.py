from django.shortcuts import render, HttpResponse, redirect

def index(request):
	if "submit_count" not in request.session:
		request.session["submit_count"] = 0
	return render(request,"survey_form/index.html")

def submit_survey_form(request):
	if request.method == "POST":
		request.session["name"] = request.POST["name"]
		request.session["location"] = request.POST["location"].replace("_"," ").title()
		request.session["favorite_language"] = request.POST["favorite_language"].replace("_"," ").title()
		request.session["comment"] = request.POST["comment"]
		request.session["submit_count"] += 1
		return redirect("/result")
	else:
		return redirect("/")

def result(request):
	return render(request,"survey_form/result.html")

def reset(request):
	del(request.session["submit_count"])
	return redirect("/")



