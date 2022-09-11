from django.contrib import admin

from handout.models.course import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ('title', 'minor')
    list_display = ('title', 'minor')
    list_display_links = ('title',)
    list_select_related = ('minor',)
    raw_id_fields = ('minor',)
    list_filter = ('minor',)
    ordering = ('minor',)
    list_per_page = 20
