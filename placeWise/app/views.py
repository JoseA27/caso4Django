from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .services import AppService, MongoDatabase
import redis
import json

# Configuración de Redis
redis_client = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB
)

# Inicializar los servicios
mongo_db = MongoDatabase()
app_service = AppService(mongo_db, redis_client)

# Vista para obtener todas las propiedades
def propiedades(request):
    if request.method == 'GET':
        data = app_service.get_propiedades()
        return JsonResponse(data, safe=False)

# Vista para crear una nueva encuesta
def create_encuesta(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        result = app_service.create_encuesta(data)
        return JsonResponse(result, status=201)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Vista para actualizar una encuesta
def update_encuesta(request, encuesta_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        result = app_service.update_encuesta(data, encuesta_id)
        return JsonResponse(result, status=200)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Vista para eliminar una encuesta
def delete_encuesta(request, encuesta_id):
    if request.method == 'DELETE':
        result = app_service.delete_encuesta(encuesta_id)
        return JsonResponse({'message': 'Encuesta eliminada'}, status=200)
    return JsonResponse({'error': 'Método no permitido'}, status=405)
