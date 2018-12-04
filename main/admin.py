from django.contrib import admin

# Register your models here.
from .models import IssueDates, Speciess, Phenophases, Forecasts

admin.site.register(Forecasts)
admin.site.register(Speciess)
admin.site.register(Phenophases)
admin.site.register(IssueDates)