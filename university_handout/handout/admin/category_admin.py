from django.contrib import admin

from handout.models.category import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_per_page = 20
