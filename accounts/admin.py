from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeFrom, CustomUserCreationFrom
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationFrom
  form = CustomUserChangeFrom
  model = CustomUser
  list_display = [
    "email",
    "username",
    "name",
    "is_staff"
  ]
  fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
  add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)

admin.site.register(CustomUser, CustomUserAdmin)