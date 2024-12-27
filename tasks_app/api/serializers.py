from rest_framework import serializers
from tasks_app.models import Task
from contacts_app.models import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    """Serializer for Contacts model."""
    class Meta:
        model = Contacts
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model with assignable contacts."""
    assignContacts = ContactsSerializer(many=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        """Creates a Task with assigned contacts."""
        assign_contacts = validated_data.pop('assignContacts', [])
        task = Task.objects.create(**validated_data)
        for contact in assign_contacts:
            contact_obj, _ = Contacts.objects.get_or_create(**contact)
            task.assignContacts.add(contact_obj)
        return task

    def update(self, instance, validated_data):
        """Updates a Task and its assigned contacts."""
        assign_contacts = validated_data.pop('assignContacts', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if assign_contacts is not None:
            instance.assignContacts.clear()
            for contact in assign_contacts:
                contact_obj, _ = Contacts.objects.get_or_create(**contact)
                instance.assignContacts.add(contact_obj)
        return instance
