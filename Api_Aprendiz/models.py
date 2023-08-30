from django.db import models

class APRENDIZ( models.Model ):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    año_nacimiento = models.PositiveIntegerField(default=0)
    tipo_documento = models.CharField(max_length=18)
    numero_ficha = models.PositiveIntegerField(default=0)
    
