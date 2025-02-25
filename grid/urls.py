from django.urls import path
from .views import home, energy_data, fetch_energy_api

urlpatterns = [
    path("", home, name="home"),  # Now accessible at /grid/
    path("fetch_energy/", fetch_energy_api, name="fetch_energy_api"),
    path("api/energy/", energy_data, name="energy_data"),  # Accessible at /grid/api/energy/
]