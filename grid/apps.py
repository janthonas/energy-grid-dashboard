from django.apps import AppConfig
import threading
import os

class GridConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "grid"

    def ready(self):
        """Start the background task thread only in the main Gunicorn process"""
        if os.environ.get("RUN_MAIN") == "true":  # Prevent multiple threads
            from .tasks import background_scheduler
            thread = threading.Thread(target=background_scheduler, daemon=True)
            thread.start()
            print("✅ Background thread started!")

    
