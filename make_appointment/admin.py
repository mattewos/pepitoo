from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'service', 'consultation', 'created_at')
    list_filter = ('service', 'consultation')
    search_fields = ('name', 'email', 'phone', 'subject')
