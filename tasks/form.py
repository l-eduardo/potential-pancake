from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completed', 'todo_list')
