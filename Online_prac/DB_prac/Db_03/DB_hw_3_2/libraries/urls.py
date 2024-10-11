from django.urls import path
from . import views

app_name = 'libraries'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:author_pk>/', views.detail, name='detail'),
]
