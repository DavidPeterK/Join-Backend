from django.urls import path
from .views import ContactListCreateView, ContactRetrieveUpdateView

urlpatterns = [
    path('list/', ContactListCreateView.as_view(),
         name='contact-list-create'),
    path('update/<int:pk>/', ContactRetrieveUpdateView.as_view(),
         name='contact-retrieve-update'),
]
