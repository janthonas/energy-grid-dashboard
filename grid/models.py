from django.db import models

class EnergyData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  # Auto store fetch time

    # Power Consumption Breakdown
    nuclear_consumption = models.FloatField()
    geothermal_consumption = models.FloatField()
    biomass_consumption = models.FloatField()
    coal_consumption = models.FloatField()
    wind_consumption = models.FloatField()
    solar_consumption = models.FloatField()
    hydro_consumption = models.FloatField()
    gas_consumption = models.FloatField()
    oil_consumption = models.FloatField()
    unknown_consumption = models.FloatField()
    hydro_discharge_consumption = models.FloatField()
    battery_discharge_consumption = models.FloatField()

    # Power Production Breakdown
    nuclear_production = models.FloatField()
    geothermal_production = models.FloatField()
    biomass_production = models.FloatField()
    coal_production = models.FloatField()
    wind_production = models.FloatField()
    solar_production = models.FloatField()
    hydro_production = models.FloatField()
    gas_production = models.FloatField()
    oil_production = models.FloatField()
    unknown_production = models.FloatField()
    hydro_discharge_production = models.FloatField()
    battery_discharge_production = models.FloatField()

    # Power Import Breakdown
    belgium_power_import = models.FloatField()
    france_power_import = models.FloatField()
    ireland_power_import = models.FloatField()
    isleofman_power_import = models.FloatField()
    netherlands_power_import = models.FloatField()
    denmark_power_import = models.FloatField()
    northern_ireland_power_import = models.FloatField()
    norway_power_import = models.FloatField()

    # Power Export Breakdown
    belgium_power_export = models.FloatField()
    france_power_export = models.FloatField()
    ireland_power_export = models.FloatField()
    isleofman_power_export = models.FloatField()
    netherlands_power_export = models.FloatField()
    denmark_power_export = models.FloatField()
    northern_ireland_power_export = models.FloatField()
    norway_power_export = models.FloatField()

    # Fossil-Free and Renewable Percentages
    fossil_free_perc = models.FloatField()
    renewable_perc = models.FloatField()

    # Total Statistics
    power_consumption_total = models.FloatField()
    power_production_total = models.FloatField()
    power_import_total = models.FloatField()
    power_export_total = models.FloatField()

    def __str__(self):
        return f"{self.timestamp} - Total Consumption: {self.power_consumption_total} MW"

