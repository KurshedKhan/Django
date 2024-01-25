from django.http import HttpResponse;
from django.shortcuts import render

def blog(request):
    return HttpResponse("This is my blog page")

def blog1(request,blogid):
    return HttpResponse(blogid)

def about(request):
    return HttpResponse("<b><u>This is my about page</b></u>")

def home(request):
    data = {
        'Tab' : 'New Tab',
        'CompanyName' : 'KhanBhaiya.com',
        'Content' : "Django Web Framework offers a shortcut to full integration with your application's database. It provides CRUD (create, read, update, delete) functionality, HttpResponse and cross-site scripting, supplies user management capabilities, offers software administration features and more",
        'Student' : ['pooja','payal','aarti','riya']
    }
    return render(request,"index.html",data)