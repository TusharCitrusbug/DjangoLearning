from django.shortcuts import redirect, render
from django.http import JsonResponse
from app.models import *

default_data={}
# Create your views here.
def All_data(request):
    pass

def home(request):
    return render(request,'app/index.html')
def login(request):
    return render(request,'app/login.html')
def success(request):
    return render(request,'app/success.html')
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

    try:
        if request.method =='POST':
            data=login_data.objects.get(email=request.POST['Email'])
            print(data)

            if data.password==request.POST['password']:
                
                request.session['email']=request.POST['Email']
                response = {
                            'msg':'welcome to your account' ,

                            'updating_form' : '''
     
    <lable for="firstname">First name: </lable>
              <input type="text" id="firstname" name="fname" value=""><BR>
    <lable for="email">email: </lable>
              <input type="text" id="emailup" name="eml" disabled><BR>
                
   <button  type="submit" id="submit" name="submit" >Update</button>
 


<div id="update_output">

</div>
<br>
<div class="login_link">
    <a href=" ">Login another account</a>
</div>
<div class="delete_link">
    
</div>
    
<br>

    

''',
'data':{
    "fname":data.name,
    "email":data.email

}
                }
                print("loginsuccess")
                return JsonResponse(response) 
            
    except:
        response = {
                    'msg':'invalid cradentials' # response message
                }
        return JsonResponse(response)   


def update_fun(request):
    # del request.session['email']
    if request.method =='POST':
        data=login_data.objects.get(email=request.session['email'])
        print(request.POST['Email'])
        data.email=request.POST['Email']
        data.name=request.POST['firstname']
        data.save()
        
        request.session['email']=request.POST['Email']
        print(f"session {request.session['email']}")
        response = {
                'data':{
                    "fname":request.POST['firstname'],
                    "email":request.POST['Email'],
                    },
                'msg':"updated successfully"
            }

    return JsonResponse(response)   


def delete_ac(request):
    pass