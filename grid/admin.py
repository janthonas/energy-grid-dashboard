from django.contrib import admin
from .models import EnergyData

@admin.register(EnergyData)
class EnergyDataAdmin(admin.ModelAdmin):
    list_display = (
        "timestamp",
        "power_consumption_total",
        "power_production_total",
        "power_import_total",
        "power_export_total",
        "fossil_free_perc",
        "renewable_perc",
    )  # Customize which fields appear in the admin list view

    search_fields = ("timestamp",)  # Enable search by timestamp
    list_filter = ("timestamp",)  # Enable filtering by timestamp
    ordering = ("-timestamp",)  # Show newest data first
