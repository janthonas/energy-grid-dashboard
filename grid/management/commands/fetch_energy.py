from django.core.management.base import BaseCommand
from grid.views import fetch_and_store_energy_data

class Command(BaseCommand):
    help = "Fetch and store energy data from the API"

    def handle(self, *args, **kwargs):
        fetch_and_store_energy_data()
        self.stdout.write(self.style.SUCCESS("Successfully fetched and stored energy data"))
