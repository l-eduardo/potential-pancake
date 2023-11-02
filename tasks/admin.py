from django.contrib import admin
from .models import TodoList, Task

# Register your models here.
admin.site.register(TodoList)
admin.site.register(Task)
