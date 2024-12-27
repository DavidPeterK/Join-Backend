from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
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


class ContactRetrieveUpdateView(RetrieveUpdateAPIView):
    """
    API view for retrieving or updating a specific contact.
    - Methods: GET (retrieve a specific contact), PUT/PATCH (update a specific contact).
    - Permissions: Requires authentication.
    """
    permission_classes = [IsAuthenticated]
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
