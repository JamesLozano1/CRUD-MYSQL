from django.urls import path
from .views import CommpanyView

urlpatterns = [
    path('companies/', CommpanyView.as_view(), name='commpany_list'),
    path('companies/', CommpanyView.as_view()),
    path('companies/put/', CommpanyView.as_view()),
    path('companies/delete/', CommpanyView.as_view()),
]