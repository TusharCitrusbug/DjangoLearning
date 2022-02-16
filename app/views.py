from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def login(request):
    return render(request,'app/index.html')
    
def login_data(request):
    if request.method == "POST":
        first_name = request.POST['firstname'] # getting data from first_name input 
        email = request.POST['Email']  # getting data from last_name input
        password = request.POST['password']  # getting data from last_name input
        print(f"{first_name} {email} {password}")
        if first_name and email and password: #cheking if first_name and last_name have value
            response = {
                         'msg':'Your form has been submitted successfully' # response message
            }
            return JsonResponse(response) # return response as JSON