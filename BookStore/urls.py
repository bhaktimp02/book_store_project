from django.urls import path, include
from . import views

app_name= "BookStore"

urlpatterns = [
	path('book-store/', views.home, name="home"),
	path('book-store/signin', views.signin, name="signin"),
	path('book-store/register', views.register, name="register"),
	#path('register_success', views.register_success, name="register_success")
]