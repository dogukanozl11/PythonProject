from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Airline
from .serializers import AirlineSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class ObtainAuthTokenView(TokenObtainPairView):
    permission_classes = ()

class AirlineListCreateView(generics.ListCreateAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    permission_classes = [IsAuthenticated]

class AirlineRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'