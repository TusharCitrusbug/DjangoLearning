
from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('registered_data/',registered_data,name="registered_data"),
    path('login/',login,name="login"),
    path('SUCCESS/',success,name="login"),

]
