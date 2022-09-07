from django.contrib import admin

from handout.models.course import Course


class CourseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course, CourseAdmin)