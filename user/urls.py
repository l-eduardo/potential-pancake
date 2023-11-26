from django.urls import path
from user.views import register, user_login, user_edit, reset_password, logout

app_name = 'user'

urlpatterns = [
    path('register/', register, name ='register'),
    path('login/', user_login, name ='login'),
    path('edit/', user_edit, name='user_edit'),
    path('logout/', logout, name='logout'),
]