from django.contrib import admin

from handout.models.professor import Professor


class ProfessorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Professor, ProfessorAdmin)