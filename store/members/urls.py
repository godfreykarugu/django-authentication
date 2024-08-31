from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('log_in/', views.log_in, name='log-in'),
    path('log_out/', views.log_out, name='log-out'),
    path('register_user/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_info/', views.update_info, name='update_info'),
   
]
