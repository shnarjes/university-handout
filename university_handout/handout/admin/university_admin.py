from django.contrib import admin

from handout.models.university import University, UniversityType


@admin.register(UniversityType)
class TypeUniAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_per_page = 20


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    search_fields = ('name', 'type')
    list_display = ('name', 'type')
    list_display_links = ('name',)
    list_select_related = ('type',)
    raw_id_fields = ('type',)
    list_filter = ('type',)
    ordering = ('type',)
    list_per_page = 20
