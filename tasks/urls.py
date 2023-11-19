from django.urls import path

from tasks.views import complete, create, delete, list_all, update, find_by_id

app_name = 'tasks'

urlpatterns = [
    path("create-task/", create, name="create"),
    path("tasks/", list_all, name="list_all"),
    path("tasks/<int:pk>/", find_by_id, name="find_by_id"),
    path("delete-task/<int:pk>/", delete, name="delete"),
    path("update-task/<int:pk>/", update, name="update"),
    path("complete-task/<int:pk>/", complete, name="complete"),
]
