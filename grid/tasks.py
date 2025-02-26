from apscheduler.schedulers.background import BackgroundScheduler
from django.utils.timezone import now
from .views import fetch_and_store_energy_data

def scheduled_task():
    """Calls fetch_and_store_energy_data() every hour"""
    print(f"[{now()}] Running scheduled task: fetch_and_store_energy_data")
    fetch_and_store_energy_data()
    print(f"✅ Energy data updated at {now()}")

# Start APScheduler
scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_task, "interval", minutes=1)  # Runs every 10mins
scheduler.start()