from django.http.response import JsonResponse
from django.views import View
from .models import Commpany
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json 

class CommpanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)    

    def get(self, request, id = 0):
        if (id > 0):
            companies = list(Commpany.objects.filter(id=id).values())
            if (len(companies) > 0):
                company = companies[0]
                datos = {'message':'Success', 'companies': companies}
            else:
                datos = {'message':'Company ot found...'}
        else:
            # companies = Commpany.objects.all() cuando es un http response
            companies = list(Commpany.objects.values())
            if len(companies) > 0:
                datos = {'message': 'Succes', 'companies': companies}
            else:
                datos = {'message': 'Commpanies not found...'}
        return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        js = json.loads(request.body)
        # print(js)
        Commpany.objects.create(name=js['name'], website=js['website'], foundation=js['fundation'])
        datos = {'menssage':'Success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        # print(jd)
        companies = list(Commpany.objects.filter(id=id).values())
        if (len(companies) > 0):
            company = Commpany.objects.get(id=id)
            print(company)
            company.name = jd['name']
            company.website = jd['website']
            company.foundation = jd['foundation']
            company.save()
            datos = {'message': 'Success'}
        else:
            datos = {'message': 'Commpanies not found...'}
        return JsonResponse(datos)

    def delete(self, request, id):
        companies = list(Commpany.objects.filter(id=id).values())
        if len(companies) > 0:
            #¿Por qué llegamso hasta acá?
            Commpany.objects.filter(id=id).delete()
            datos = {'message': 'Success'}
        else:
            datos = {'message': 'Company bot found...'}
        
        return JsonResponse(datos)

        

