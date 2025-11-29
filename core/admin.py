from django.contrib import admin
from .models import Category, Task

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'color',
        'created_at'
    )
    search_fields = ('title',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'deadline',
        'is_completed',
        'category',
        'user',
        'created_at',
        'updated_at'
    )
    list_filter = ('is_completed', 'category__title', 'user__username')
    search_fields = ('title', 'description')