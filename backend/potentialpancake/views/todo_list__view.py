from rest_framework import viewsets
import sys
sys.path.append('../..')
from tasks.models import TodoList
from tasks.serializers import TodoListSerializer


class TodoListView(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()
