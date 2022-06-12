from django.contrib import admin
from .models import Anime, Category

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']

class AnimeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created']

admin.site.register(Anime, AnimeAdmin),
admin.site.register(Category, CategoryAdmin)