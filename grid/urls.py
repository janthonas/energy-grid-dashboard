from django.urls import path
from .views import home, energy_data, fetch_energy_api, get_energy_averages, get_production_consumption_source

urlpatterns = [
    path("", home, name="home"),  # Now accessible at /grid/
    path("fetch_energy/", fetch_energy_api, name="fetch_energy_api"),
    path("api/energy/", energy_data, name="energy_data"),  # Accessible at /grid/api/energy/
    path("api/energy-averages/", get_energy_averages, name="get_energy_averages"),
    path('api/production_consumption_source/', get_production_consumption_source, name='get_production_consumption_source')
]