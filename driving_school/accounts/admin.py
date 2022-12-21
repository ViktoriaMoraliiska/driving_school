from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from driving_school.accounts.forms import UserEditForm, UserCreateForm


@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    form = UserEditForm
    add_form = UserCreateForm
