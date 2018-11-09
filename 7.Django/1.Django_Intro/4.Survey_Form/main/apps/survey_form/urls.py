from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^survey_form$',views.index),
	url(r'^submit_survey_form$',views.submit_survey_form),
	url(r'^result$',views.result),
	url(r'^reset$',views.reset)
]

