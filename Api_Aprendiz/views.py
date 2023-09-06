from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Aprendiz
from .forms import AgregarAprendiz

def index( request ):
    title = 'Api Aprendices'
    return render( request, 'index.html', {
        'title': title,
    })

def aprendiz( request ):
    aprendiz = list(Aprendiz.objects.values())
    titulo = 'Aprendices'
    return render(request, 'Aprendiz/aprendiz.html', {
        'titulo':titulo,
        'aprendiz':aprendiz,
    })

# def aprendiz(request):
#     pass


def crear_Aprendiz( request ):
    if request.method == 'GET':
        return render( request, 'Aprendiz/crear_aprendiz.html', {
            'form':crearAprendiz(),
        })
    else:
        form = crearAprendiz(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            año_nacimiento = form.cleaned_data['año_nacimiento']
            numero_documento = form.cleaned_data['numero_documento']
            tipo_documento = form.cleaned_data['tipo_documento']
            numero_ficha = form.cleaned_data['numero_ficha']
            Aprendiz.objects.create(nombre=nombre, apellido=apellido, año_nacimiento=año_nacimiento, numero_documento=numero_documento, tipo_documento=tipo_documento, numero_ficha=numero_ficha)
            return redirect('/aprendiz')
    return HttpResponse("Success!")












# # class aprendicesView(View):
#     @method_decorator(csrf_exempt)
#     def dispatch( self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
    
#     def getaprendiz(self, request, id = 0):
#         if (id > 0):
#             aprendices = list(Aprendiz.objects.filter(id=id).values())
#             if len(aprendices) > 0:
#                 aprendiz = aprendices[0]
#                 datos = {'mensaje':'éxito', 'aprendices': aprendices}
#             else:
#                 datos = {'mensaje':'aprendiz no encontrado...'}
#         else:
#             aprendices = list(Aprendiz.objects.values())
#             if len(aprendices) > 0:
#                 datos = {'mensaje':'éxito', 'aprendices': aprendices}
#             else:
#                 datos = {'mensaje':'aprendices no encontrados...'}
#         return JsonResponse(datos)


#     def postAprendiz(self, request):
#         js = json.loads(request.body)
#         Aprendiz.objects.create(nombre=js['Nombre'], apellido=js['Apellido'], año_nacimiento=js['Año nacimiento'], tipo_documento=js['Tipo documento'], numero_ficha=js['Numero de ficha'])
#         datos = {'mensaje':'Éxito'}
#         return JsonResponse(datos)

#     def putAprendiz():
#         pass


#     def deleteAprendiz():
#         pass



