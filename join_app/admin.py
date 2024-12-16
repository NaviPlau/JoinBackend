from django.contrib import admin
from join_app.models import Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'category', 'column', 'dueDate')
    search_fields = ('title', 'description')
    list_filter = ('priority', 'category', 'column')
