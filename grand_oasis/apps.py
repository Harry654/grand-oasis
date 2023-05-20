from django.apps import AppConfig


class GrandOasisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'grand_oasis'

    def ready(self):
        import grand_oasis.signals