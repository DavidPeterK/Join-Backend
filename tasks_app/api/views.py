from tasks_app.models import Task
from .serializers import TaskSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from tasks_app.models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

# API für alle Tasks (GET & POST)


class TaskListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# API für eine einzelne Task (GET, PUT, PATCH)


class TaskRetrieveUpdateView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
