from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('change_password/', views.change_password, name='change_password'),
]