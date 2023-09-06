from django import forms
from .models import Aprendiz

# class crearAprendiz(forms.Form):
#     TIPOS_DOCUMENTO = (
#         ('CC', 'Cédula de Ciudadanía'),
#         ('TI', 'Tarjeta de Identidad'),
#         ('CE', 'Cédula de Extranjería'),
#         ('PA', 'Pasaporte'),
#     )

#     nombre = forms.CharField(max_length=50)
#     apellido = forms.CharField(max_length=50)
#     año_nacimiento = forms.IntegerField()
#     numero_documento = forms.CharField(max_length=20)
#     tipo_documento = forms.ChoiceField(choices=TIPOS_DOCUMENTO)
#     numero_ficha = forms.CharField(max_length=10)

class AgregarAprendiz( forms.Form ):
    TIPOS_DOCUMENTO = (
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte'),
    )
    nombre =forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    año_nacimiento = forms.IntegerField()
    numero_documento = forms.CharField(max_length=20)
    tipo_documento = forms.CharField(widget=forms.Select(choices=TIPOS_DOCUMENTO))
