from django.apps import AppConfig

class DrinksAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drinks_app'
    
    def ready(self):
        import drinks_app.signals
    
    
