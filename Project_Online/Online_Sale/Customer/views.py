from django.shortcuts import render,redirect
from .models import RegisterData
from .forms import RegisterForm,LoginForm
# Create your views here.
def ShowIndex(request):
	return render(request,"CustomerTemp/customer.html")

def ShowRegister(request):
	form = RegisterForm()

	return render(request,"CustomerTemp/register.html",{"form":form})

def SaveUser(request):
	massage = ""
	RegForm = RegisterForm()
	if request.method=="POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			contact = form.cleaned_data['contact']
			address = form.cleaned_data['address']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			RegisterData(name=name,contact=contact,address=address,email=email,password=password).save()
			massage = "Registration  Successfull"
			return render(request,"CustomerTemp/register.html",{"form":RegForm,"massage":massage})
	return render(request,"CustomerTemp/register.html",{"form":RegForm,"massage":massage})


def LoginPage(request):
	form = LoginForm()
	return render(request,"CustomerTemp/login.html",{"form":form})

def LoginInto(request):
	msg = ""
	form = LoginForm()
	if request.method=="POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['Userid']
			password = form.cleaned_data['Password']
			user = RegisterData.objects.filter(email=username,password = password)
			if user:
				response =  redirect("Register")
				response.set_cookie("status", True)
				return response
			else:
				msg = "invalid Crediantials"
	return render(request,"CustomerTemp/login.html",{"form":form,"massage":msg})


















