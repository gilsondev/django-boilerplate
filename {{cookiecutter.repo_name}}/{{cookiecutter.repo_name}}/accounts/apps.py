from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = "{{cookiecutter.repo_name}}.accounts"
    default_auto_field = "django.db.models.BigAutoField"
