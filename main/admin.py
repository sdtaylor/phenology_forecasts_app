from django.contrib import admin

# Register your models here.
from .models import IssueDates, Speciess, Phenophases, Forecasts

@admin.register(IssueDates)
class IssueDatesAdmin(admin.ModelAdmin):
    list_display = ('issue_date','display_text')
    
@admin.register(Speciess)
class SpeciessAdmin(admin.ModelAdmin):
    list_display = ('species', 'display_text','default')

@admin.register(Phenophases)
class PhenophasesAdmin(admin.ModelAdmin):
    list_display = ('phenophase', 'display_text','default')

@admin.register(Forecasts)
class ForecastsAdmin(admin.ModelAdmin):
    list_display = ('issue_date','phenophase','species')
