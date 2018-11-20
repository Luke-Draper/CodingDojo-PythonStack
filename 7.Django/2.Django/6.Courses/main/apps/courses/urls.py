from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$',views.index),
	url(r'^courses$',views.index),
	url(r'^courses/(?P<id>\d+)/destroy$',views.destroy),
	url(r'^courses/(?P<id>\d+)/destroy/real$',views.destroy_real),
	url(r'^post$',views.post)
]

