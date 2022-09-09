from django.contrib import admin
from jalali_date import datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin
from django.utils.translation import gettext_lazy as _

from handout.models.handout import Handout


@admin.register(Handout)
class Handoutadmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'university',
        'professor',
        'get_created_jalali',
    )
    readonly_fields = (
        'get_created_jalali',
        'upload_datetime',
        'modify_datetime',
    )
    list_filter = (
        'category',
        'professor',
        'university',
        'add_datetime',
        'modify_datetime'
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
        'add_datetime',
        'category',
    )
    raw_id_fields = (
        'category',
        'university',
        'professor',
        'course'
    )
    date_hierarchy = 'add_datetime'
    list_select_related = (
        'category',
        'university',
        'professor',
        'course'
    )
    list_per_page = 20

    @admin.display(description=_('add_time'), ordering='created')
    def get_created_jalali(self, obj):

        return datetime2jalali(obj.add_datetime).strftime('%y/%m/%d _ %H:%M:%S')
