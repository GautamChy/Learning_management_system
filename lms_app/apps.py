from django.apps import AppConfig


class LmsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lms_app'
    
    
    def ready(self):
        import lms_app.signals

            
