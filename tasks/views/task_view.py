from django.http import HttpResponse
from rest_framework import viewsets
from django.template import loader

from ..models import Task
from ..serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


    def get(self, request):
        all_tasks = Task.objects.all()
        template = loader.get_template("tasks/get_tasks.html")
        context = {
            "all_tasks": all_tasks,
        }
        return HttpResponse(template.render(context, request))