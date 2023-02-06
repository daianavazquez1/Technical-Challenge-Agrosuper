from django.contrib import admin
from django.urls import path, include
from . import views
#from .views import *

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('salir/', views.salir, name='salir'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('carnes/', views.DatosCarnes.as_view(), name='carnes'),
    path('variaciones/', views.obtenerVariaciones, name='variaciones'),
    path('editor/', views.editorSemanal, name='editor'),
    path('editarVariable/', views.EditaryProbarVariable, name='editaryprobar'),
]