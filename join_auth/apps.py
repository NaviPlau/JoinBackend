from django.apps import AppConfig


class JoinAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'join_auth'

    def ready(self):
        import join_auth.signals