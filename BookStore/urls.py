from django.urls import path
from . import views

app_name= "BookStore"

urlpatterns = [
	path('book-store/', views.home, name="home"),
	path('book-store/signin/', views.signin, name="signin"),
	path('book-store/register/', views.register, name="register"),
]