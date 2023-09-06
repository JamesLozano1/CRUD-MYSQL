from django.db import models

class Aprendiz(models.Model):
    TIPOS_DOCUMENTO = (
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte'),
    )

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    año_nacimiento = models.IntegerField()  # Set default here
    numero_documento = models.CharField(max_length=20)
    tipo_documento = models.CharField(max_length=2, choices=TIPOS_DOCUMENTO)
    numero_ficha = models.CharField(max_length=10)

    def __str__(self):
        return f"Aprendiz {self.nombre} {self.apellido}"
