from django.core.cache import cache
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from app.models import Propiedades
from app.serializers import PropiedadesSerializer
import hashlib


# Helper function to create a unique cache key
def get_cache_key(*args, **kwargs):
    query_string = str(args) + str(kwargs)
    return hashlib.md5(query_string.encode("utf-8")).hexdigest()


# Vista para obtener todas las propiedades con caché
@csrf_exempt
def propiedades(request, id=0):
    if request.method == "GET":
        cache_key = get_cache_key("propiedades", id)
        cached_data = cache.get(cache_key)

        if cached_data:
            return JsonResponse(cached_data, safe=False)

        # Si no está en caché, consulta la base de datos
        propiedades = Propiedades.objects.filter(Ciudad__in=["Alajuela", "San José"])
        propiedades_serializer = PropiedadesSerializer(propiedades, many=True)
        response_data = propiedades_serializer.data

        # Guardar el resultado en caché
        cache.set(cache_key, response_data)

        return JsonResponse(response_data, safe=False)


# Vista para obtener propiedades con parámetros usando caché
@csrf_exempt
def propiedadesParametro(request, id=0):
    if request.method == "GET":
        ciudades = request.GET.getlist("ciudad")
        cache_key = get_cache_key("propiedadesParametro", ciudades)

        cached_data = cache.get(cache_key)

        if cached_data:
            return JsonResponse(cached_data, safe=False)

        # Si no está en caché, consulta la base de datos
        if ciudades:
            propiedades = Propiedades.objects.filter(Ciudad__in=ciudades)
        else:
            propiedades = Propiedades.objects.all()

        propiedades_serializer = PropiedadesSerializer(propiedades, many=True)
        response_data = propiedades_serializer.data

        # Guardar el resultado en caché
        cache.set(cache_key, response_data)

        return JsonResponse(response_data, safe=False)
