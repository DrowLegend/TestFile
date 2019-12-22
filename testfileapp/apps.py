from django.apps import AppConfig


class TestfileConfig(AppConfig):
    name = 'testfileapp'

    def ready(self):
        import testfileapp.signals


