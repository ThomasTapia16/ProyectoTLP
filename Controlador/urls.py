from django.contrib import admin
from django.urls import path
from . import login

urlpatterns = [
    path('',login.logging,name = 'logging')
]
