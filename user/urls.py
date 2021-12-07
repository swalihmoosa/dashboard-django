from django.urls import path
from user.views import user


app_name = "user"


urlpatterns = [
    path('', user, name="user" )
]