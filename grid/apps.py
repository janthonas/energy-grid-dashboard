from django.apps import AppConfig
import threading
import os

class GridConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "grid"

    
