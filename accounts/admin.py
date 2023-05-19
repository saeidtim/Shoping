from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomCreateForms, CustomChangeForms


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomCreateForms
    form = CustomChangeForms
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'age', 'img', )}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', 'age', 'img',)}),
    )

