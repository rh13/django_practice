from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def home(request):
	return render(request, 'base.html')

def index(request):
	return render(request, 'index.html')

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request,user)
			return render(request, 'base.html')
		else: 
			return HttpResponse("Username or password incorrect")
	return render(request, 'login.html')

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def user_signup(request):
	form = UserCreationForm()
	if request.method == "POST": # jokhon post hobe tokhon ei kajgula hobe
		form = UserCreationForm(request.POST) # form e je datagula chilo oigula eivaba nite hoy
		if form.is_valid(): # erpor dekhte hobe datagula valid ki na  (jemon password match korche ki na, username onek sort ki na, emon habijabi)
			form.save() # sob thik thakle save dite hobe, na hoile user create hobe na, login o korte parba na
			return HttpResponseRedirect('/login') # eita je kono kichu hoite pare, ami just signup korle sign in page e niye jabe eita korchi. tumi oi page eo rakhte paro. ei line kono fact na

	return render(request, 'signup.html',{'signup_form':form}) 