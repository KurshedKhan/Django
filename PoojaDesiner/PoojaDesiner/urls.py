"""
URL configuration for PoojaDesiner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PoojaDesiner import views

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('blog/', views.blog),
    path('blog/<blogid>',views.blog1),
    path('', views.home),
    path('about/', views.about,name="about-us"),
    path('service/', views.service),
    path('contact-us/', views.contact),
    path('UserForm/', views.Userform),
    path('SubmitForm/', views.sumitform),
    path('DjangoForm/',views.djangoform),
    path('OddEven/',views.oddeven),
     path('Marksheet/',views.marksheet)
      
]
