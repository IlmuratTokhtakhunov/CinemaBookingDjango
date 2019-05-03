"""Booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from App import views
urlpatterns = [
	path('', views.Auth),
	path('admin/', views.admin),
	path('user/', views.user),
	path('user/profU/', views.profU),
	path('user/viewB/', views.viewB),
	path('user/buyT/', views.buyT),
	path('reg/', views.Reg),
	path('admin/addmov/', views.addMov),
	path('admin/addcin/', views.addcin),
	path('admin/addsch/', views.addsch),
	path('admin/viewM/', views.viewM),
	path('admin/viewC/', views.viewC),
	path('admin/viewS/', views.viewS),
	path('admin/viewT/', views.viewT),
	path('admin/prof/', views.profA),
	path('user/buyT/find/', views.find),
]
