from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	
    path('order/', views.order, name='order'),
     
] 