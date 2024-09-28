from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('propiedades/', views.propiedades, name='propiedades'),
    path('propiedadesParametro/', views.propiedadesParametro, name='propiedadesParametro'),
    path('propiedadesPool/', views.propiedadesPool, name='propiedadesPool'),
    path('propiedadesRedis/', views.propiedadesRedis, name='propiedadesRedis'),
    path('propiedadesRedisYPool/', views.propiedadesRedisYPool, name='propiedadesRedisYPool'),
]
