from django.contrib import admin
from .models import Location, DailyTemp

# Register your models here.
# Registering these models with admin lets us modify, update, and destroy data from within the admin interface.
# The admin interface is a powerful feature, we have options to expand here.

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(DailyTemp)
class DailyTempAdmin(admin.ModelAdmin):
    pass