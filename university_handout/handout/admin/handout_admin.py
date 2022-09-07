from django.contrib import admin

from handout.models.handout import Handout


@admin.register(Handout)
class Handoutadmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'university',
        'professor',
        'upload_datetime',
    )
    list_filter = (
        'category',
        'professor',
        'university',
        'add_datetime'
    )
    search_fields = (
        'title',
        'category',
        'professor',
        'university',
        'source',
        'author',
        'description',
    )
    list_display_links = ('title',)
    ordering = (
        'upload_datetime',
        'category',
    )
    raw_id_fields = (
        'category',
        'university',
        'professor',
        'course'
    )
    date_hierarchy = 'upload_datetime'
    list_select_related = (
        'category',
        'university',
        'professor',
        'course'
    )
    list_per_page = 20
