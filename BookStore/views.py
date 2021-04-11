from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
	template = loader.get_template('BookStore/home.html')
	return HttpResponse(template.render({},request))

def signin(request):
	template = loader.get_template('BookStore/signin.html')
	return HttpResponse(template.render({},request))

def register(request):
	template = loader.get_template('BookStore/register.html')
	return HttpResponse(template.render({},request))
	
