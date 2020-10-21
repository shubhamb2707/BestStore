from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
def register(request):
	if request.method == "POST":
		import pdb; pdb.set_trace()
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		email = request.POST.get("email")
		password = request.POST.get("password")
		confirm_password = request.POST.get("confirm_password")
		if password == confirm_password:
			data=User()
			data.first_name = first_name
			data.last_name = last_name
			data.email = email
			data.password = make_password(password)
			data.save()
			return redirect('/user/login/')
		else:
			var = "confirm_password wrongh please resubmit form"
			return render(request, "register.html",{"var":var})

	else:
		return render(request,"register.html")

def Login_View(request):
	if request.method == 'POST':

		#import pdb; pdb.set_trace()
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(email=email, password=password)
		if user is not None:
			login(request, user)
			LoginName = request.user.first_name
			return render(request,"index.html",{"LoginName":LoginName})
		else:
			return render(request, "login.html")

	else:
		return render(request,"login.html")


from django.contrib import auth
def Logout_View(request):
    auth.logout(request)
    return render(request,'index.html')



def index(request):
	return render(request, "index.html")

