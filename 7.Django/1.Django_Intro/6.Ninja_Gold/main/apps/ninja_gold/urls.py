from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$',views.index),
	url(r'^find_gold$',views.find_gold),
	url(r'^reset$',views.reset)
]

