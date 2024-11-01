from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # 원래 서비스라면 index를 없애도 무방
    path('save_data/', views.save_data)
]
