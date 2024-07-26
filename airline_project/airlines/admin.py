from django.contrib import admin
from .models import Airline

@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ['name', 'callsign', 'founded_year', 'base_airport']
    search_fields = ['name', 'callsign','founded_year','base_airport']