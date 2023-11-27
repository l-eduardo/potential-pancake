from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name ='register'),
    path('login/', views.user_login, name ='login'),
    path('edit/', views.user_edit, name='user_edit'),
    path('edit-password/', views.change_password, name='edit_password'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('logout/', views.logout, name ='logout'),
]