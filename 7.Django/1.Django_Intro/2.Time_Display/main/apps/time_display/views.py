from django.shortcuts import render, HttpResponse, redirect
from time import strftime, gmtime
import collections
# the index function is called when root is visited
def index(request):
	context = {
		"current_date": strftime("%b %d, %Y",gmtime()),
		"current_time": strftime("%I:%M %p",gmtime())
	}
	print(context)
	return render(request,"time_display/index.html",context)

