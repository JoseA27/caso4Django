from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connection
from app.models import Propiedades
from app.serializers import PropiedadesSerializer


from django.core.files.storage import default_storage

# Configuración de Redis
"""redis_client = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB
)
"""


# Vista para obtener todas las propiedades 
@csrf_exempt
def propiedades(request,id=0):
    if request.method=='GET':
        propiedades = Propiedades.objects.filter(Ciudad__in=['Alajuela','San José'])
        propiedades_serializer=PropiedadesSerializer(propiedades,many=True)
        return JsonResponse(propiedades_serializer.data,safe=False)
    
@csrf_exempt
def propiedadesParametro(request,id=0):
    if request.method == 'GET':
        ciudades = request.GET.getlist('ciudad')  # Obtener una lista de ciudades desde los parámetros GET
        if ciudades:
            propiedades = Propiedades.objects.filter(Ciudad__in=ciudades)  # Filtrar propiedades en varias ciudades
        else:
            propiedades = Propiedades.objects.all()  # Si no hay ciudades en la solicitud, devolver todas las propiedades
        
        propiedades_serializer = PropiedadesSerializer(propiedades, many=True)
        return JsonResponse(propiedades_serializer.data, safe=False)
    
@csrf_exempt
def propiedadesPool(request,id=0):
    if request.method == 'GET':
        ciudades = request.GET.getlist('ciudad')  # Obtener una lista de ciudades desde los parámetros GET
        
        # Usamos una conexión del pool
        with connection.cursor() as cursor:
            if ciudades:
                propiedades = Propiedades.objects.filter(Ciudad__in=ciudades)  # Filtrar propiedades por ciudades
            else:
                propiedades = Propiedades.objects.all()  # Si no hay ciudades, obtener todas las propiedades
        propiedades_serializer = PropiedadesSerializer(propiedades, many=True)
        return JsonResponse(propiedades_serializer.data, safe=False)

