from django.urls import path
from user.views import register, user_login, reset_password

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name ='register'),
    path('login/', views.user_login, name ='login'),
    path('user/edit/', views.user_edit, name='user_edit'),
]