from django.contrib import admin

from handout.models.handout import Handout


class Handoutadmin(admin.ModelAdmin):
    list_display = ('title', 'category','university', 'professor', 'upload_datetime',)
    list_filter = ('category', 'professor', 'university',)
    search_fields = ('title', 'category', 'professor', 'university', 'source', 'author', 'description',)
    list_display_links = ('title',)
    ordering = ('upload_datetime','category',)
    raw_id_fields = ('category', 'university', 'professor', 'course')
    date_hierarchy = 'upload_datetime'

admin.site.register(Handout, Handoutadmin)