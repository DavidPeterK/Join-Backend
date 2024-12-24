from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from contacts_app.models import Contacts
from .serializers import ContactsSerializer
from rest_framework.permissions import IsAuthenticated


class ContactListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactRetrieveUpdateView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
