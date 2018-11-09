from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
	if "word_count" not in request.session:
		request.session["word_count"] = 1
	else:
		request.session["word_count"] += 1
	request.session["word"] = get_random_string(length=14)
	return render(request,"random_word/index.html")

def reset(request):
	del request.session["word_count"]
	return redirect("/random_word")
