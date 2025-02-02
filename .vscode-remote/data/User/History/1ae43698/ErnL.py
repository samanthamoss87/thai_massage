from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'available_times')
    fields = ('title', 'description', 'duration', 'available_times')


admin.site.register(Service, ServiceAdmin)
