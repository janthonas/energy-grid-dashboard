import threading
import time
import requests
from django.utils.timezone import now
from .views import fetch_and_store_energy_data

def background_scheduler():
    """Runs fetch_and_store_energy_data() every 10 minutes & pings the app"""
    while True:
        print(f"[{now()}] Running scheduled task: fetch_and_store_energy_data")
        fetch_and_store_energy_data()
        print(f"✅ Energy data updated at {now()}")

        # Keep the app alive by pinging itself
        try:
            requests.get("https://energy-grid-dashboard.onrender.com")
            print("✅ Pinged Render app to prevent sleep")
        except requests.exceptions.RequestException:
            print("❌ Failed to ping Render app")

        time.sleep(6)  # Sleep for 10 minutes
