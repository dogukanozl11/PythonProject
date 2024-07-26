from django.db import models
from airlines.models import Airline

class Aircraft(models.Model):
    manufacturer_serial_number = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    operator_airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    number_of_engines = models.PositiveIntegerField()

    def _str_(self):
        return self.manufacturer_serial_number