from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name ='register'),
    path('login/', views.user_login, name ='login'),
    path('user/edit/', views.user_edit, name='user_edit'),
]