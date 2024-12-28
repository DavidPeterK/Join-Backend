from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from contacts_app.models import Contacts
from .serializers import ContactsSerializer
from rest_framework.permissions import IsAuthenticated


class ContactListCreateView(ListCreateAPIView):
    """
    API view for listing all contacts and creating a new contact.
    - Methods: GET (list all contacts), POST (create a new contact).
    - Permissions: Requires authentication.
    """
    permission_classes = [IsAuthenticated]
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a specific contact.
    - Methods: GET, PUT/PATCH, DELETE.
    - Permissions: Requires authentication.
    """
    permission_classes = [IsAuthenticated]
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
