from django.urls import path
from user.views import register, user_login, reset_password

app_name = 'user'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('reset-password/', reset_password, name='reset_password'),
]