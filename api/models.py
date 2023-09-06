from django.db import models

class Commpany( models.Model ):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    foundation = models.PositiveIntegerField(default=0
    )

# MODELAR UN APRENDIZ QUE VA A TENER UN NOMBRE UN APELLIDO UN AÑO DE NACIEMIENTO UN NUMERO DE DOCUMENTO UN TIPO DE DOCUMENTO NUMERO DE FICHA 
