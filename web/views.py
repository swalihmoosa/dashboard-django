from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from user.views import user_login


# @login_required()

def index(request):
    if "username" in request.session:
        return render(request, "index.html")
    else:
        return redirect("user/")