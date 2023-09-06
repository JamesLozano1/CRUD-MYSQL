from django.urls import path
from . import views 

urlpatterns = [ 
    path('home', views.index, name='home' ),
    path('Crear_aprendiz', views.crear_Aprendiz, name='Crear_aprendiz'),
    path('aprendiz', views.aprendiz, name='aprendiz'),
#     path('aprendices/<int:id>', aprendicesView.as_view()),
#     path('aprendices/put/<int:id>', aprendicesView.as_view()),
]