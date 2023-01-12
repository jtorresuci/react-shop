from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    # Configuring app so it knows about the signal
    def ready(self):
        import base.signals