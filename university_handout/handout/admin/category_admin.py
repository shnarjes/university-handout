from django.contrib import admin

from handout.models.category import Category


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    
    
    

admin.site.register(Category, CategoryAdmin)