from django.conf.urls import url,include
urlpatterns = [
	url(r'^', include('apps.semi_restful_users.urls'))
]

