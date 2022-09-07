from django.contrib import admin

from handout.models.major_minor import Major, Minor


class MinorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Minor, MinorAdmin)

class MajorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Major, MajorAdmin)