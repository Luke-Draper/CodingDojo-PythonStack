from django.conf.urls import url,include
urlpatterns = [
	url(r'^', include('apps.dojo_ninjas.urls'))
]

