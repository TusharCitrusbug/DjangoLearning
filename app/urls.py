
from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('',login,name="login"),
    path('',login_data,name="login_data"),
]
