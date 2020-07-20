from django.contrib import admin
from .models import Location, DailyTemp

# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(DailyTemp)
class DailyTempAdmin(admin.ModelAdmin):
    pass