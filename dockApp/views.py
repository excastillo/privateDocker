from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.
def mainLogin(request):

    if 'loginForm' in request.POST:
        uName=request.POST["username"]
        pword=request.POST["password"]
        print("LOGIN")
        user = authenticate(request, username = uName, password=pword)
        if user is not None:
            login(request, user)
            return render(request, "loginS.html", {"userName":uName} )
        else:
            return render(request, "loginE.html", {"userName":uName})
    
    return render(request, "index.html")
def mainRegister(request):
    if 'signupForm' in request.POST:
        uName=request.POST["username"]
        pword=request.POST["password"]
        user = User.objects.create_user(username = uName, first_name= "NULL", last_name= "NULL", email="NULL", password = pword)
        user.save()
        print("SIGNUP")
        return render(request, "/")
    return render(request, "register.html")