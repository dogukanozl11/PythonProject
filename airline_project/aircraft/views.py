from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Aircraft
from .serializers import AircraftSerializer

class AircraftListCreateView(generics.ListCreateAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    permission_classes = [IsAuthenticated]

class AircraftRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    permission_classes = [IsAuthenticated]