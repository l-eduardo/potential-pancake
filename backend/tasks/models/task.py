from django.db import models
from .todo_list import TodoList


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField()
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
