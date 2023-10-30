from django.urls import path, include
from rest_framework import routers
from .views import TodoListView, TaskView


router = routers.DefaultRouter()
router.register(r'todo-lists', TodoListView, 'todo-list')
router.register(r'tasks', TaskView, 'task')

urlpatterns = [
    path('api/', include(router.urls)),
]
