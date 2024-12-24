from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView

urlpatterns = [
    path('list/', TaskListCreateView.as_view(), name='task-list'),
    path('edit/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(),
         name='task-retrieve-update-destroy'),
]
