from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateView

urlpatterns = [
    path('list/', TaskListCreateView.as_view(), name='task-list'),
    path('edit/<int:pk>/', TaskRetrieveUpdateView.as_view(),
         name='task-retrieve-update'),
]
