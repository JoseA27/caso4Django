from rest_framework import serializers
from app.models import Propiedades

class PropiedadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedades
        fields = (
            'ID_de_Propiedad',
            'Ciudad',
            'Provincia',
            'Tipo_de_Propiedad',
            'Precio_CRC',
            'Descripción'
        )

