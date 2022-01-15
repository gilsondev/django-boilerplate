from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = "{{cookiecutter.project_module}}.accounts"
    default_auto_field = "django.db.models.BigAutoField"
