from django.apps import AppConfig


# Configuration for the app, it prepares the app to run
class ClassappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'classApp'
