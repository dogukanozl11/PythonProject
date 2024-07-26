from django.db import models

class Airline(models.Model):
    name = models.CharField(max_length=255)
    callsign = models.CharField(max_length=100)
    founded_year = models.PositiveIntegerField()
    base_airport = models.CharField(max_length=100)

    def _str_(self):
        return self.name 