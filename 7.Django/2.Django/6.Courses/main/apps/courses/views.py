from django.shortcuts import render, HttpResponse, redirect
from .models import Course

def index(request):
	context={"courses": Course.objects.all()}
	return render(request,"courses/index.html",context)

def post(request):
	if request.method == "POST" and len(request.POST["name"])>=5 and len(request.POST["description"])>=15:
		c = Course(name=request.POST["name"],description=request.POST["description"])
		c.save()
		return redirect("/courses")
	else:
		return redirect("/courses")

def destroy(request, id):
	context = {"course" : Course.objects.get(id=id)}
	return render(request,"courses/delete.html",context)

def destroy_real(request, id):
	c = Course.objects.get(id=id)
	c.delete()
	return redirect("/courses")