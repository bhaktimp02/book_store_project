from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import UserInfo
from .forms import UserInfoForm

from django.views import View

# Create your views here.

# Home Page View
def home(request):
	template = loader.get_template('BookStore/home.html')
	return HttpResponse(template.render({},request))


#Sign In View
def signin(request):
	template = loader.get_template('BookStore/signin.html')
	return HttpResponse(template.render({},request))


#Sign Up (Register) View
def register(request):
	form = UserInfoForm(request.POST)
	if form.is_valid():
		user_name = form.cleaned_data.get("UserName")
		print(user_name)
		form.save()
		context = {'user_name':user_name}
		return render(request, 'BookStore/userpage.html',context)

	context = {
		'form' : form,
		
	}
	template = loader.get_template('BookStore/register.html')
	return HttpResponse(template.render(context,request))



def register_success(request):
	return HttpResponse("Successfully Registerd")
	
# class UserInfoView(View):
# 	form_class = UserInfoForm
# 	inital = {'key' : 'value'}
# 	template_name = 'BookStore/signup.html'

# 	def get(self, request, *args, **kwargs):
# 		form = self.form_class(inital=self.inital)
# 		return render(request,self.template_name,{'form':form})


# 	def post(self, request, *args, **kwargs):
# 		form = self.form_class(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponse("Successfully Signed Up")

# 		return render(request, self.template_name,{'form' : form})









	
