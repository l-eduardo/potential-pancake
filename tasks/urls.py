from django.urls import path

from tasks.views import complete_task, create_task, delete_task, list_tasks, update_task, find_task_by_id

app_name = 'tasks'

urlpatterns = [
    path("create-task/", create_task, name="create_task"),
    path("tasks/", list_tasks, name="list_tasks"),
    path("tasks/<int:pk>/", find_task_by_id, name="find_task_by_id"),
    path("delete-task/<int:pk>/", delete_task, name="delete_task"),
    path("update-task/<int:pk>/", update_task, name="update_task"),
    path("complete-task/<int:pk>/", complete_task, name="complete_task"),
]
