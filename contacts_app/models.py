from django.db import models


class Contacts(models.Model):
    """
    Represents a contact with optional name, abbreviation, phone, and color.
    Email is required.
    """
    name = models.CharField(max_length=50, blank=True, null=True)
    nameAbbreviation = models.CharField(max_length=3, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.nameAbbreviation})"
