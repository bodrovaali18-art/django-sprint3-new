from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'category',
        'location',
        'pub_date',
        'is_published',
    ]
    search_fields = [
        'title',
        'text',
    ]
    list_filter = [
        'category',
        'location',
        'is_published',
    ]
