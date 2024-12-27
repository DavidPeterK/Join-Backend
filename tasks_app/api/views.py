from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from tasks_app.models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated


class TaskListCreateView(ListCreateAPIView):
    """
    API view for listing and creating tasks.
    Requires authentication.
    """
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a task.
    Requires authentication.
    """
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
