from django.http import HttpResponse
from django.shortcuts import render,redirect

def blog(request):
    return HttpResponse("This is my blog page")

def blog1(request,blogid):
    return HttpResponse(blogid)

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')

def Userform(request):
   data = {}
   try:
       if request.method == "POST" :
           n1 = int(request.POST['num1'])
           n2 = int(request.POST['num2'])
           total = n1 + n2;
           print("\n================================\n")
           print("My n1 Value : ",n1)
           print("My n2 Value : ",n2)
           print("My Total Value : ",total)
           print("\n================================\n")

           data = {
                "value1" : n1,
                "value2" : n2,
                "output" : total
           }
           return redirect('/about/')
   except:
       pass
    
   return render(request,"UserForm.html",data)


def sumitform(request):
    data = {}
    try:
       if request.method == "POST" :
           n1 = int(request.POST['num1'])
           n2 = int(request.POST['num2'])
           total = n1 + n2;
           print("\n================================\n")
           print("My n1 Value : ",n1)
           print("My n2 Value : ",n2)
           print("My Total Value : ",total)
           print("\n================================\n")

           data = {
                "value1" : n1,
                "value2" : n2,
                "output" : total
           }
           return render(request,"SubmitForm.html",data)
    except:
        pass
    
    return render(request,"UserForm.html",data)


def home(request):
   data = {}
   try:
       if request.method == "GET" :
            name = request.GET.get('name')
            phoneNumber = request.GET['phoneNumber']
            email = request.GET['email']
            messagebox = request.GET['messagebox']
            data = {
                "name" : name,
                "phoneNumber" : phoneNumber,
                'email' : email,
                'messagebox' : messagebox
                
            }
            return redirect("/about/")
   except:
       pass
    
   return render(request,"index.html",data)