# from django.apps import AppConfig


# class TestappConfig(AppConfig):
#     name = 'testapp'
from django.apps import AppConfig

class testappConfig(AppConfig):
    name = "testapp"

    def ready(self):
        import testapp.documents
