from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name ='register'),
    path('login/', views.user_login, name ='login'),
    path('user/edit/', views.user_edit, name='user_edit'),
]