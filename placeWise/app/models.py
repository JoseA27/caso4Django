from django.db import models

class Propiedades(models.Model):
    #ID = models.AutoField(primary_key=True)
    ID_de_Propiedad = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length=100)
    Provincia = models.CharField(max_length=100)
    Tipo_de_Propiedad = models.CharField(max_length=100)
    Precio_CRC = models.DecimalField(max_digits=12, decimal_places=2)
    Descripción = models.TextField()

    class Meta:
        db_table = 'propiedades'