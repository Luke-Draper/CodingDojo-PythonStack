from django.shortcuts import render, HttpResponse, redirect
from .models import User

# def redirect(request):
# 	del request.session["dummy"]
# 	return redirect("/")

# def post(request):
# 	if request.method == "POST":
# 		request.session["name"] = request.POST["name"]
# 		print("")
# 		print(request.POST)
# 		print(request.POST["name"])
# 		print(request.POST["desc"])
# 		print("")
# 		return redirect("/")
# 	else:
# 		return redirect("/")

# context = {
# 	"dummy": "dummy"
# }
# request.session["dummy"] = "dummy"
# return render(request,"semi_restful_users/index.html",context)

def index(request):
	context = {"flash":False}
	if "flash" in request.session and request.session["flash"] == True:
		context["flash"] = True
		context["flash_type"] = request.session["flash_type"]
		context["flash_msg"] = request.session["flash_msg"]
		request.session["flash"] = False
	context["users"] = User.objects.all()
	return render(request,"semi_restful_users/users.html",context)

def new(request):
	context = {"flash":False}
	if "flash" in request.session and request.session["flash"] == True:
		context["flash"] = True
		context["flash_type"] = request.session["flash_type"]
		context["flash_msg"] = request.session["flash_msg"]
		request.session["flash"] = False
	
	return render(request,"semi_restful_users/new_user.html",context)

def edit(request, id):
	context = {"flash":False}
	if "flash" in request.session and request.session["flash"] == True:
		context["flash"] = True
		context["flash_type"] = request.session["flash_type"]
		context["flash_msg"] = request.session["flash_msg"]
		request.session["flash"] = False
	
	context["user"] = User.objects.get(id=id)

	return render(request,"semi_restful_users/edit_user.html",context)

def show(request, id):
	context = {"flash":False}
	if "flash" in request.session and request.session["flash"] == True:
		context["flash"] = True
		context["flash_type"] = request.session["flash_type"]
		context["flash_msg"] = request.session["flash_msg"]
		request.session["flash"] = False
	
	context["user"] = User.objects.get(id=id)

	return render(request,"semi_restful_users/show_user.html",context)

def create(request):
	request.session["flash"] = True
	if request.method == "POST":
		u = User(first_name=request.POST["first_name"],last_name=request.POST["last_name"], email=request.POST["email"])
		u.save()
		request.session["flash_type"] = "success"
		request.session["flash_msg"] = "Succesfully created a user"
	else:
		request.session["flash_type"] = "danger"
		request.session["flash_msg"] = "Unable to create user"
	
	return redirect("/users/new")

def destroy(request, id):
	request.session["flash"] = True
	request.session["flash_type"] = "success"
	u = User.objects.get(id=id)

	request.session["flash_msg"] = "Succesfully deleted " + u.first_name + " " + u.last_name

	u.delete()
	return redirect("/users")

def update(request):
	request.session["flash"] = True
	if request.method == "POST":
		u_id = request.POST["id"]
		u = User.objects.get(id=u_id)
		if request.POST["first_name"] != "":
			u.first_name=request.POST["first_name"]
		if request.POST["last_name"] != "":
			u.last_name=request.POST["last_name"]
		if request.POST["email"] != "":
			u.email=request.POST["email"]
		u.save()
		request.session["flash_type"] = "success"
		request.session["flash_msg"] = "Succesfully updated " + u.first_name + " " + u.last_name
		return redirect("/users/"+u_id)
	else:
		request.session["flash_type"] = "danger"
		request.session["flash_msg"] = "Unable to update user"
		return redirect("/users")
	
