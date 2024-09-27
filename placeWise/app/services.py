from pymongo import MongoClient
from django.conf import settings
import redis

class MongoDatabase:
    def __init__(self):
        self.client = MongoClient(settings.MONGO_URI)
        self.database = self.client["PropiedadesDB"]
        self.collection = self.database["propiedades"]

    def _convert_object_ids(self, data):
        if "_id" in data:
            data["_id"] = str(data["_id"])

    def insert_propiedad(self, propiedad_data):
        self._convert_object_ids(propiedad_data)
        self.collection.insert_one(propiedad_data)

    def get_propiedades(self):
        propiedades = list(self.collection.find({}))
        for propiedad in propiedades:
            self._convert_object_ids(propiedad)
        return propiedades

    def get_propiedad_by_id(self, propiedad_id):
        propiedad = self.collection.find_one({"ID de Propiedad": propiedad_id})
        if propiedad:
            self._convert_object_ids(propiedad)
            return propiedad
        else:
            return False

    def update_propiedad(self, propiedad_id, updated_propiedad_data):
        self._convert_object_ids(updated_propiedad_data)
        result = self.collection.update_one(
            {"ID de Propiedad": propiedad_id}, {"$set": updated_propiedad_data}
        )
        if result.modified_count > 0:
            return updated_propiedad_data
        else:
            return None

    def delete_propiedad(self, propiedad_id):
        result = self.collection.delete_one({"ID de Propiedad": propiedad_id})
        return result.deleted_count
    

class AppService:
    def __init__(self, mongo_database: MongoDatabase, redis_client: redis.StrictRedis):
        self.mongo_database = mongo_database
        self.redis_client = redis_client

    def clear_cache(self, cache_key):
        try:
            self.redis_client.delete(cache_key)
        except Exception as e:
            print(f"Error al limpiar la caché: {e}")

    def get_propiedades(self):
        return self.mongo_database.get_propiedades()

    def get_encuesta_by_ID(self, encuesta_id):
        return self.mongo_database.get_propiedad_by_id(encuesta_id)

    def create_encuesta(self, encuesta):
        self.mongo_database.insert_propiedad(encuesta)
        self.clear_cache("propiedades")
        return encuesta

    def update_encuesta(self, updated_encuesta, encuesta_id):
        self.mongo_database.update_propiedad(encuesta_id, updated_encuesta)
        self.clear_cache("propiedades")
        return updated_encuesta

    def delete_encuesta(self, encuesta_id):
        self.clear_cache("propiedades")
        self.mongo_database.delete_propiedad(encuesta_id)
        return encuesta_id