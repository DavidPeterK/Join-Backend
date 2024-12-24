from rest_framework import serializers
from tasks_app.models import Task
from contacts_app.models import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    assignContacts = ContactsSerializer(many=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        assign_contacts_data = validated_data.pop('assignContacts', [])
        task = Task.objects.create(**validated_data)
        for contact_data in assign_contacts_data:
            contact, created = Contacts.objects.get_or_create(**contact_data)
            task.assignContacts.add(contact)
        return task

    def update(self, instance, validated_data):
        assign_contacts_data = validated_data.pop('assignContacts', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if assign_contacts_data is not None:
            instance.assignContacts.clear()  # Alte Kontakte entfernen
            for contact_data in assign_contacts_data:
                contact, created = Contacts.objects.get_or_create(
                    **contact_data)
                instance.assignContacts.add(contact)

        return instance
