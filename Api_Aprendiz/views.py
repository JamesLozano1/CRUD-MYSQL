from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from .models import APRENDIZ
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class aprendicesView(View):
    @method_decorator(csrf_exempt)
    def dispatch( self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    pass
