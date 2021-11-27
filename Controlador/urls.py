from django.contrib import admin
from django.urls import path
from . import login,views

urlpatterns = [
    path('',login.logging,name = 'logging'),
    path('AgregarUsuario',login.adduser,name = 'adduser')
    #path('registrar',)
]
