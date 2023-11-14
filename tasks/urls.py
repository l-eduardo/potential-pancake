from django.urls import path

from tasks.views import complete_task, create_task, delete_task, list_tasks

urlpatterns = [
    path("create-task/", create_task, name="create_task"),
    path("tasks/", list_tasks, name="list_tasks"),
    path("delete-task/<int:pk>/", delete_task, name="delete_task"),
    path("complete-task/<int:pk>/", complete_task, name="complete_task"),
]
