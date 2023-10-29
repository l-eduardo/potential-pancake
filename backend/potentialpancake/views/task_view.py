from rest_framework import viewsets
import sys
sys.path.append('../..')
from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
