from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,"index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        FirstName = request.POST['FirstName']
        SecondName = request.POST['SecondName']
        Email = request.POST['Email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.get(username=username):
            messages.error(request,"username already exits.")
            return render(request,"signup.html")
        MyUser = User.objects.create_user(username,Email,password1)
        MyUser.first_name = FirstName
        MyUser.last_name = SecondName
        MyUser.save()

        # messages.success(request,"My user is created Successfully.!")
        return redirect("signin")
    
    return render(request,"signup.html")

def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            # messages.error(request,"Your Username and Password are not matched.")
            return redirect("signin")
    return render(request,"signin.html")

def signout(request):
    logout(request)
    # messages.success(request,"Your are logout successfully 😊.")
    return redirect('signin')