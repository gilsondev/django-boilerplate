from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # noqa
from {{cookiecutter.project_module}}.accounts.models import User

admin.site.register(User)
