from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse



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
def propiedades(request):
    if request.method == 'GET':
        
        return None
    
@csrf_exempt
def propiedades(request,id=0):
    if request.method=='GET':
        propiedades = Propiedades.objects.all()
        propiedades_serializer=PropiedadesSerializer(propiedades,many=True)
        return JsonResponse(propiedades_serializer.data,safe=False)
