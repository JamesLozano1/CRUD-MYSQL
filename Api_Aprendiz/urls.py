from django.urls import path
from .views import aprendicesView

urlpatterns = [ 
    path('aprendices/', aprendicesView.as_view()),
    
]