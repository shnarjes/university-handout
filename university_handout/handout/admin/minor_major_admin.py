from django.contrib import admin

from handout.models.major_minor import Major, Minor


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_per_page = 20


@admin.register(Minor)
class MinorAdmin(admin.ModelAdmin):
    search_fields = ('title', 'major')
    list_display = ('title', 'major')
    list_display_links = ('title',)
    list_select_related = ('major',)
    raw_id_fields = ('major',)
    list_filter = ('major',)
    ordering = ('major',)
    list_per_page = 20
