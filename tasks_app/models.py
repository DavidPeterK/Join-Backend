from django.db import models
from contacts_app.models import Contacts


class Task(models.Model):
    """
    Represents a task with details like status, category, priority, 
    assigned contacts, and subtasks.
    """
    status = models.CharField(max_length=20, default='')
    category = models.CharField(max_length=50, default='')
    categoryColor = models.CharField(max_length=30, default='')
    title = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=355, default='')
    dueDate = models.CharField(max_length=50, default='')
    priority = models.CharField(max_length=10, default='')
    assignContacts = models.ManyToManyField(
        Contacts, related_name="assignedTasks", default=list)
    subtasksInProgress = models.JSONField(default=list)
    subtasksFinish = models.JSONField(default=list)

    def __str__(self):
        return f"{self.title} ({self.status})"
