from django.urls import include, path
from . import views

app_name= "BookStore"

urlpatterns = [
	path('', views.home, name="home"),
]