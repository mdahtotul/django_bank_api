from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from custom_auth.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
  add_fieldsets = (
    (
      None,
      {
        'classes': ('wide',),
        'fields': (
          'username',
          'first_name',
          'last_name',
          'email',
          'password1',
          'password2',
        )
      }
    )
  )
