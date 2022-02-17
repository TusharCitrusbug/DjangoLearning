
from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('registered_data/',registered_data,name="registered_data"),
    path('login/',login,name="login"),
    path('login_fun/',login_fun,name="login_fun"),
    path('SUCCESS/',success,name="login"),
    path('update/',update_fun,name="update-fun"),
    path('delete_ac/',delete_ac,name="delete_ac"),

]
