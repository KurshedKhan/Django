from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import Djangoform

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
           n1 = eval(request.POST['num1'])
           n2 = eval(request.POST['num2'])
           opr = request.POST['opr']
           if opr == "+":
               total = n1 + n2
           elif opr == "-":
               total = n1-n2
           elif opr == "*":
               total = n1*n2
           elif opr == "/":
               total = n1/n2
           data = {
                "value1" : n1,
                "value2" : n2,
                "output" : total
           }
        
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

def djangoform(request):
    fn = Djangoform()
    data = {'form' : fn}
    try:
       if request.method == "POST" :
           n1 = int(request.POST['num1'])
           n2 = int(request.POST['num2'])
           total = n1 + n2;
           data = {
                "value1" : n1,
                "value2" : n2,
                "output" : total,
                'form' : fn
           }
           return render(request,"SubmitForm.html",data)
    except:
        pass
    
    return render(request,"DjangoForm.html",data)






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

def oddeven(request):
    try:
        result = '';
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            if n1 % 2 == 0:
                result = "Even Number"
            else:
                result = "Odd Number"
        return render(request,'OddEven.html',{"Output" : result})
    except:
        pass

    
def marksheet(request):
    Std_data = {}
    Total = 0
    P = 0
    Div = ""
    try:
        if request.method == "POST":
            Hindi = eval(request.POST['Hindi'])
            English = eval(request.POST['English'])
            Maths = eval( request.POST['Maths'])
            Science = eval(request.POST['Science'])
            SST = eval(request.POST['SST'])
            Total = Hindi + English + Maths + Science + SST
            P = (Total * 100)/ 500

            if P>90:
                Div = "First Division"
            elif P> 70:
                Div = "Second Division"  
            elif P>45:
                Div = "Third Division"  
            Std_data = {
                "Output" : Total,
                "PRC" : P,
                "Division" : Div,
            }
    except:
        pass
        


    return render(request,'Marksheet.html',Std_data)