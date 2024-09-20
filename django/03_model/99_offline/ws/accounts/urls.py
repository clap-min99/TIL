from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('index/', views.main, name='main'),
]
