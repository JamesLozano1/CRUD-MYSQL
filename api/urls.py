from django.urls import path
from .views import CommpanyView

urlpatterns = [
    path('companies/', CommpanyView.as_view(), name='commpany_list'),
    path('companies/<int:id>', CommpanyView.as_view()),
    path('companies/put/<int:id>', CommpanyView.as_view()),
    # path('companies/delete/', CommpanyView.as_view()),
]