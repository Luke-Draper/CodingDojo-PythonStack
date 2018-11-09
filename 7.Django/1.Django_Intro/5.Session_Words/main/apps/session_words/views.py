from django.shortcuts import render, HttpResponse, redirect
from time import strftime, gmtime

def index(request):
	if "words" not in request.session:
		new_array = []
		request.session["words"] = new_array
	return render(request,"session_words/index.html")

def reset(request):
	del request.session["words"]
	return redirect("/")

def post(request):
	if request.method == "POST":
		new_word = {
			"word": request.POST["word"],
			"color": request.POST["color"],
			"big": "2rem" if (request.POST["big_font"]=="1") else "1rem",
			"datetime":strftime("%I:%M:%S%p, %b %d, %Y",gmtime())
		}
		word_array = request.session["words"]
		word_array.append(new_word)
		request.session["words"] = word_array
		return redirect("/")
	else:
		return redirect("/")

