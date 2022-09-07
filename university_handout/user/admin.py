from django.contrib import admin

from user.models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = (
        'first_name',
        'last_name',
        'phone',
        'email',
    )
    list_display = (
        'first_name',
        'last_name',
        'phone',
    )
    list_display_links = (
        'first_name',
        'phone'
    )
    list_per_page = 20
