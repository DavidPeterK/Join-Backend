# tasks_app/admin.py
from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'dueDate', 'priority')
    filter_horizontal = ('assignContacts',)
