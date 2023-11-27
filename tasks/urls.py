from django.urls import path

from tasks.views import complete, create, create_task_to_card, delete, list_all, update, find_by_id

app_name = 'tasks'

urlpatterns = [
    path('create-task/', create, name='create'),
    path('tasks/', list_all, name='list_all'),
    path('tasks/<int:pk>/', find_by_id, name='find_by_id'),
    path('task-to-card/<int:pk>/', create_task_to_card, name='create_task_to_card'),
    path('delete-task/<int:pk>/', delete, name='delete'),
    path('update-task/<int:pk>/', update, name='update'),
    path('complete-task/<int:pk>/', complete, name='complete'),
]
