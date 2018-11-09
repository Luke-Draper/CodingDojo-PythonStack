from django.conf.urls import url,include

urlpatterns = [
	url(r'^', include('apps.survey_form.urls'))
]

