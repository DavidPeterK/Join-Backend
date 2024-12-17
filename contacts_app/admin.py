# contacts_app/admin.py
from django.contrib import admin
from .models import Contacts


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'color')
