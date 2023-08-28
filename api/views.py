from django.http.response import JsonResponse
from django.views import View
from .models import Commpany

class CommpanyView(View):
    def get(self, request):
        # companies = Commpany.objects.all() cuando es un http response
        companies = list(Commpany.objects.values())
        if len(companies) > 0:
            datos = {'message': 'Succes', 'companies': companies}
        else:
            datos = {'message': 'Commpanies not found...'}
        return JsonResponse(datos)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

