from django.urls import path
from .views import ContactListCreateView, ContactRetrieveUpdateDestroyView

urlpatterns = [
    path('list/', ContactListCreateView.as_view(),
         name='contact-list-create'),
    path('update/<int:pk>/', ContactRetrieveUpdateDestroyView.as_view(),
         name='contact-retrieve-update'),
]
