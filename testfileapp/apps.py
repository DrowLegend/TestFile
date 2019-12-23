from django.apps import AppConfig


class TestfileConfig(AppConfig):
    name = 'testfileapp'

# запуск сигналов
    def ready(self):
        import testfileapp.signals


