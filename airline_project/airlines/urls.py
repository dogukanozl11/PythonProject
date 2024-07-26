from django.urls import path
from .views import (
    AirlineListCreateView,
    AirlineRetrieveUpdateDestroyView,
    
)

urlpatterns = [
    path('airlines/', AirlineListCreateView.as_view(), name='airline-list-create'),
    path('airlines/<int:pk>/', AirlineRetrieveUpdateDestroyView.as_view(), name='airline-detail'),
]