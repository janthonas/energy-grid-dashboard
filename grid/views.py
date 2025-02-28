import requests
from django.shortcuts import render
from .models import EnergyData
import json
from django.http import JsonResponse
from django.conf import settings

import time
from django.utils.timezone import now

def home(request):
    """Show the latest energy data"""
    latest_data = EnergyData.objects.order_by("-timestamp").first()
    return render(request, "grid/index.html", {"latest_data": latest_data})

def fetch_and_store_energy_data():
    """Fetch energy data from API and save it to the database"""
    power_breakdown = requests.get(
        "https://api.electricitymap.org/v3/power-breakdown/latest?zone=GB",
        headers={
            "auth-token": settings.ELECTRICITY_MAP_AUTH_TOKEN
        }
    )
    
    if power_breakdown.status_code == 200:
        full_energy_json = power_breakdown.json()

        # Create a new EnergyData entry
        def get_value(dictionary, key):
            return dictionary.get(key, 0) if dictionary.get(key) is not None else 0

        EnergyData.objects.create(
            # Power Consumption Breakdown
            nuclear_consumption=get_value(full_energy_json['powerConsumptionBreakdown'], 'nuclear'),
            geothermal_consumption=get_value(full_energy_json['powerConsumptionBreakdown'], 'geothermal'),
            biomass_consumption=get_value(full_energy_json['powerConsumptionBreakdown'], 'biomass'),
            coal_consumption=get_value(full_energy_json['powerConsumptionBreakdown'], 'coal'),
            wind_consumption=get_value(full_energy_json['powerConsumptionBreakdown'], 'wind'),
            solar_consumption=get_value(full_energy_json['powerConsumptionBreakdown'], 'solar'),
            hydro_consumption=get_value(full_energy_json['powerConsumptionBreakdown'], 'hydro'),
            gas_consumption=get_value(full_energy_json['powerConsumptionBreakdown'], 'gas'),
            oil_consumption=get_value(full_energy_json['powerConsumptionBreakdown'], 'oil'),
            unknown_consumption=get_value(full_energy_json['powerConsumptionBreakdown'], 'unknown'),
            hydro_discharge_consumption=get_value(full_energy_json['powerConsumptionBreakdown'], 'hydro discharge'),
            battery_discharge_consumption=get_value(full_energy_json['powerConsumptionBreakdown'], 'battery discharge'),

            # Power Production Breakdown
            nuclear_production=get_value(full_energy_json['powerProductionBreakdown'], 'nuclear'),
            geothermal_production=get_value(full_energy_json['powerProductionBreakdown'], 'geothermal'),
            biomass_production=get_value(full_energy_json['powerProductionBreakdown'], 'biomass'),
            coal_production=get_value(full_energy_json['powerProductionBreakdown'], 'coal'),
            wind_production=get_value(full_energy_json['powerProductionBreakdown'], 'wind'),
            solar_production=get_value(full_energy_json['powerProductionBreakdown'], 'solar'),
            hydro_production=get_value(full_energy_json['powerProductionBreakdown'], 'hydro'),
            gas_production=get_value(full_energy_json['powerProductionBreakdown'], 'gas'),
            oil_production=get_value(full_energy_json['powerProductionBreakdown'], 'oil'),
            unknown_production=get_value(full_energy_json['powerProductionBreakdown'], 'unknown'),
            hydro_discharge_production=get_value(full_energy_json['powerProductionBreakdown'], 'hydro discharge'),
            battery_discharge_production=get_value(full_energy_json['powerProductionBreakdown'], 'battery discharge'),

            # Power Import Breakdown
            belgium_power_import=get_value(full_energy_json['powerImportBreakdown'], 'BE'),
            france_power_import=get_value(full_energy_json['powerImportBreakdown'], 'FR'),
            ireland_power_import=get_value(full_energy_json['powerImportBreakdown'], 'IE'),
            isleofman_power_import=get_value(full_energy_json['powerImportBreakdown'], 'IM'),
            netherlands_power_import=get_value(full_energy_json['powerImportBreakdown'], 'NL'),
            denmark_power_import=get_value(full_energy_json['powerImportBreakdown'], 'DK-DK1'),
            northern_ireland_power_import=get_value(full_energy_json['powerImportBreakdown'], 'GB-NIR'),
            norway_power_import=get_value(full_energy_json['powerImportBreakdown'], 'NO-NO2'),

            # Power Export Breakdown
            belgium_power_export=get_value(full_energy_json['powerExportBreakdown'], 'BE'),
            france_power_export=get_value(full_energy_json['powerExportBreakdown'], 'FR'),
            ireland_power_export=get_value(full_energy_json['powerExportBreakdown'], 'IE'),
            isleofman_power_export=get_value(full_energy_json['powerExportBreakdown'], 'IM'),
            netherlands_power_export=get_value(full_energy_json['powerExportBreakdown'], 'NL'),
            denmark_power_export=get_value(full_energy_json['powerExportBreakdown'], 'DK-DK1'),
            northern_ireland_power_export=get_value(full_energy_json['powerExportBreakdown'], 'GB-NIR'),
            norway_power_export=get_value(full_energy_json['powerExportBreakdown'], 'NO-NO2'),

            # Fossil-Free and Renewable Percentages
            fossil_free_perc=get_value(full_energy_json, 'fossilFreePercentage'),
            renewable_perc=get_value(full_energy_json, 'renewablePercentage'),

            # Total Statistics
            power_consumption_total=get_value(full_energy_json, 'powerConsumptionTotal'),
            power_production_total=get_value(full_energy_json, 'powerProductionTotal'),
            power_import_total=get_value(full_energy_json, 'powerImportTotal'),
            power_export_total=get_value(full_energy_json, 'powerExportTotal')
        )
        
        return "Data stored successfully"

    return "Failed to fetch data"

def fetch_energy_api(request):
    # Get API key from request headers
    api_key = request.headers.get("X-API-KEY")

    # Validate API key
    if api_key != settings.FETCH_ENERGY_API_KEY:
        return JsonResponse({"error": "Unauthorized"}, status=403)

    # Run your function if the key is correct
    from .views import fetch_and_store_energy_data
    fetch_and_store_energy_data()
    return JsonResponse({"status": "success", "message": "Data updated!"})


def energy_data(request):
    """Returns the latest stored energy data as JSON"""
    latest_data = EnergyData.objects.order_by("-timestamp").first()
    
    if latest_data:
        data = {
            "timestamp": latest_data.timestamp,
            "nuclear_consumption": latest_data.nuclear_consumption,
            "solar_production": latest_data.solar_production,
            "power_consumption_total": latest_data.power_consumption_total,
            "power_production_total": latest_data.power_production_total,
        }
        return JsonResponse(data, safe=False)
    
    return JsonResponse({"error": "No energy data available"}, status=404)

