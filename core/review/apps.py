from django.apps import AppConfig


class ReviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'review'

    def ready(self) -> None:
        import review.signals
        return super().ready()
