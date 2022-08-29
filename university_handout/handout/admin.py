from django.contrib import admin

from handout.models.category import Category
from handout.models.course import Course
from handout.models.handout import Handout
from handout.models.major_minor import Major, Minor
from handout.models.professor import Professor
from handout.models.university import UniversityType, University


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Minor)
admin.site.register(Major)
admin.site.register(Professor)
admin.site.register(University)
admin.site.register(UniversityType)
admin.site.register(Handout)
