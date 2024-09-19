from django.urls import path
from . import views

app_name = 'todos'
# 관리의 용이성을 위해 이름을 붙이자


urlpatterns = [
    # main 경로로 요청이 들어오면 todos 앱 패키지 안에 있는 
    # views.py 모듈 안에 있는 main함수를 실행시켜줘
    path('main/', views.main, name = 'main'),
    # 사용자가 todo를 만들고 싶어하는구나
    # todo를 추가할 수 있는 기능이 포함된 함수를 만들고, 
    # todo를 추가할 수 있는 html을 반환하자
    path('create/', views.create, name = 'create'),
]