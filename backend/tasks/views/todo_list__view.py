from rest_framework import viewsets
from ..models import TodoList
from ..serializers import TodoListSerializer


class TodoListView(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()
