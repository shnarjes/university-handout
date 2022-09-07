from django.contrib import admin

from handout.models.professor import Professor


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_per_page = 20
