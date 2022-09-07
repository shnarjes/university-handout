from django.contrib import admin

from handout.models.university import University, UniversityType


class TypeUniAdmin(admin.ModelAdmin):
    pass

admin.site.register(UniversityType, TypeUniAdmin)


class UniversityAdmin(admin.ModelAdmin):
    pass

admin.site.register(University, UniversityAdmin)
