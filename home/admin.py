from django.contrib import admin
from .models import User,  Task

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'mobile')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'task_type', 'status', 'created_at', 'completed_at')
    search_fields = ('name', 'task_type', 'status')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)
    filter_horizontal = ('assigned_users',)  