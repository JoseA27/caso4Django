from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('propiedades/', views.propiedades, name='propiedades'),
    path('propiedadesParametro/', views.propiedadesParametro, name='propiedadesParametro'),
]
