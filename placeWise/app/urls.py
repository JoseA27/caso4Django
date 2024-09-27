from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('propiedades/', views.propiedades, name='propiedades'),
    path('encuestas/', views.create_encuesta, name='create_encuesta'),
    path('encuestas/<str:encuesta_id>/', views.update_encuesta, name='update_encuesta'),
    path('encuestas/<str:encuesta_id>/delete/', views.delete_encuesta, name='delete_encuesta'),
]