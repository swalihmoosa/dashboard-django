from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def user_login(request):
    if request.method == 'POST':

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)

        if user is not None:
            request.session['username'] = username
            return redirect("/")

    return render(request, "login.html")


def user_logout(request):
    if "username" in request.session:
        del request.session['username']
    return redirect('/')
