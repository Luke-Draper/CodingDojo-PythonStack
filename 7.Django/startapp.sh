#!/bin/bash
source "$HOME/Documents/Projects/Coding_Dojo/Python_Stack/0.Virtual_Environments/djangoPy3Env/bin/activate"

echo ""

django-admin startproject main

cd main

mkdir apps

cd apps

touch __init__.py

python ../manage.py startapp "$1"

# echo 'add the line : "app.'"$1"'", : after the line : INSTALLED_APPS = [ : in main/main/settings.py before running the server'
# echo ""
# sed '/INSTALLED_APPS = [/a "app.'"$1"'",'

cd ../

python manage.py makemigrations
python manage.py migrate

mkdir "./apps/$1/templates"
mkdir "./apps/$1/templates/$1"
touch "./apps/$1/templates/$1/index.html"
touch "./apps/$1/urls.py"

echo '<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>Title</title>
		<meta name="description" content="Description" />
		<link
			rel="stylesheet"
			href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
			integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
			crossorigin="anonymous"
		/>
		<script
			src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
			integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
			crossorigin="anonymous"
		></script>
		<script
			src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"
			integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
			crossorigin="anonymous"
		></script>
		<script
			src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"
			integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"
			crossorigin="anonymous"
		></script>
	</head>
	<body>
		<div class="container">
			<h1>Example Page</h1>
			<form action="/post" method="post">
				{% csrf_token %}
				<label for="name">Name:</label>
				<input type="text" id="name" name="name" placeholder="Name">
				<label for="desc">Description:</label>
				<textarea id="desc" name="desc" placeholder="description"></textarea>
				<button type="submit">Submit</button>
			</form>
		</div>
	</body>
</html>' > "./apps/$1/templates/$1/index.html"

echo 'from django.conf.urls import url,include

urlpatterns = [
	url(r'"'"'^'"'"', include('"'"'apps.'"$1"'.urls'"'"'))
]
' > './main/urls.py'


echo 'from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'"'"'^$'"'"',views.index)
	url(r'"'"'^redirect$'"'"',views.redirect)
	url(r'"'"'^post$'"'"',views.post)
]
' > "./apps/$1/urls.py"


echo 'from django.shortcuts import render, HttpResponse, redirect

def index(request):
	context = {
		"dummy": "dummy"
	}
	request.session["dummy"] = "dummy"
	return render(request,"'"$1"'/index.html",context)

def redirect(request):
	del request.session["dummy"]
	return redirect("/")

def post(request):
	if request.method == "POST":
			print("")
			print(request.POST)
			print(request.POST["name"])
			print(request.POST["desc"])
			print("")
			return redirect("/")
	else:
			return redirect("/")

' > "./apps/$1/views.py"

echo ""
echo 'add the line : "app.'"$1"'", : after the line : INSTALLED_APPS = [ : in main/main/settings.py before running the server'
echo ""
echo 'cd into main and run : python manage.py runserver : to start '
echo ""
