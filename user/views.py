from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")


    return render(request, "login.html")
