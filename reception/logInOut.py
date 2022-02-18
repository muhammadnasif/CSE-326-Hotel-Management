from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .views import home as reception_home


def LogIn(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect(reception_home)
        else:
            return redirect(LogIn)
    else:
        return render(request, 'CommonHTML/LogIn.html')


def LogOut(request):
    logout(request)
    return redirect(LogIn)
