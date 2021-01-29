from django.apps import AppConfig

class AppNameConfig(AppConfig):
    name = 'your_app_name'
    def ready(self):
        from scheduler import scheduler
        scheduler.start()