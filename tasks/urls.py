from django.urls import path, include
from rest_framework import routers
from .views import TodoListView, TaskView


router = routers.DefaultRouter()
router.register(r'todo-lists', TodoListView, 'todo-list')

urlpatterns = [
    path('api/', include(router.urls)),
    path(
        'task/',
         TaskView.as_view({"get": "get", "post": "create"}),
         name="get__all_task"
         )
]