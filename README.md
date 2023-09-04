# Django
## Django Command in python 

1. pip install virtualenv
2. virtualenv envname(MyEnv)
3. MyEnv\scripts\activate
4. pip install django
5. django-admin
6. django-admin startproject projectName(BookStore)
7. code .
8. cd BookStore
9. python manage.py runserver
10. how to runserver break
	ctrl + c (runserver break)
11. clear = cls
12. django-admin startapp applicationName(Book)
13. python manage.py runserver
=====================================================
===================================================== <br>
#### apne ko do kaam karne hote hai 
	1.
		1. project ke ander setting file me jao
		2. setting file me installed list me jana
		3. applicationname.apps.applicationconfig
		exp. (Book.apps.Bookconfig)
	2. 
		1. sabse phle apn application me urls.py file bnaye
		2. fir project me jate hai
	=======================================================		
		from django.contrib import admin
		from django.urls import path,include

		urlpatterns = [
    		path('admin/', admin.site.urls),
   		path("",include("Book.urls")),
		]
	=======================================================

	3. fir application ke url me jate hai
	======================================================
		from django.urls import path
		from . import views
		urlpatterns = [
   		path("",views.home,name="home")
		]
	=====================================================
	4. fir views file  me jana hai
	====================================================
	from django.shortcuts import render
	from django.http import HttpResponse
	# Create your views here.

	def home(request):
   	  return HttpResponse("Hello World...!")
	======================================================
