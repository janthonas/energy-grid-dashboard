from django.apps import AppConfig
import os

class GridConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "grid"
    
    def ready(self):
        """Ensure scheduler runs only in the main process"""
        if os.environ.get("RUN_MAIN") == "true":  # Prevent multiple schedulers
            from .tasks import scheduler
    
