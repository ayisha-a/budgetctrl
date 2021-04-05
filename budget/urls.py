"""Budgetctrlsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import registration,signin,signout,expense_create,view_expense,edit_expense,delete_expense,create_category,review_expense
from django.shortcuts import render


urlpatterns = [
    path("",lambda request:render(request,"budget/base.html")),
    path('registration',registration,name="registration"),
    path('signin',signin,name="signin"),
    path('signout',signout,name="signout"),
    path("addexpens",expense_create,name="addexpens"),
    path("viewexpen",view_expense,name="viewexpense"),
    path("editexpense/<int:id>",edit_expense,name="editexpense"),
path("deleteexpense/<int:id>",delete_expense,name="deleteexpense"),
    path("category",create_category,name="category"),
    path("review",review_expense,name="review")
]
