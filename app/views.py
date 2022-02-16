from django.shortcuts import render
from django.http import JsonResponse
from .models import *

default_data={}
# Create your views here.
def All_data(request):
    pass

def home(request):
    return render(request,'app/index.html')
def login(request):
    return render(request,'app/login.html')

# create operation 
  
def registered_data(request):
   
    if request.method == "POST":
        
        first_name = request.POST['firstname'] # getting data from first_name input 
        email = request.POST['Email']  # getting data from last_name input
        password = request.POST['password']  # getting data from last_name input
        print(f"first_name:{first_name} email:{email} password:{password}")
        if first_name and email and password: #cheking if first_name and last_name have value
            response = {
                         'msg':f'Dear {first_name}Your have registrated  successfully ' # response message
            }
            data=login_data.objects.create(
                name=first_name,
                email=email,
                password=password,
            )

            return JsonResponse(response) # return response as JSON

# login page
def login_fun(request):
    if request.method =='POST':
        pass