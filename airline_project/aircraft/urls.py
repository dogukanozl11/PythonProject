from django.urls import path
from .views import (
    AircraftListCreateView,
    AircraftRetrieveUpdateDestroyView
)

urlpatterns = [
    path('aircrafts/', AircraftListCreateView.as_view(), name='aircraft-list-create'),
    path('aircrafts/<int:pk>/', AircraftRetrieveUpdateDestroyView.as_view(), name='aircraft-detail'),
]