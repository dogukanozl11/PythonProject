from django.contrib import admin
from .models import Aircraft

@admin.register(Aircraft)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ['manufacturer_serial_number', 'type', 'model', 'operator_airline', 'number_of_engines']

    search_fields = ['manufacturer_serial_number','type']