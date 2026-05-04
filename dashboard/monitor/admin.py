from django.contrib import admin
from .models import SensorData

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'temperature', 'pressure', 'status', 'timestamp')
    list_filter = ('status',)
    search_fields = ('status',)