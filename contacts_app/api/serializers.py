from rest_framework import serializers
from contacts_app.models import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contacts model.
    Converts Contacts model instances to JSON format and vice versa.
    Includes all fields from the Contacts model.
    """
    class Meta:
        """
        Meta class to specify model and fields for the serializer.
        """
        model = Contacts
        fields = '__all__'
