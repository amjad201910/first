from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'phone',
        'country',
        'number_of_free_message',
        'dateOfStart',
        'group',
        'Money_transfer_image',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    list_filter = (
        'last_login',
        'dateOfStart',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    raw_id_fields = ('groups', 'user_permissions')