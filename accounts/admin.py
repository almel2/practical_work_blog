from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import UserModel


@admin.register(UserModel)
class AdminUser(UserAdmin):
    pass
