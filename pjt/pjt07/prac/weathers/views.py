from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response
from django.conf import settings

from .models import Weather
from .serializers import WeatherSerializer
# Create your views here.

# 1. OpenWeatherMap API로부터 데이터 다운로드 
# 2. 그대로 출력 

@api_view(['GET'])
def index(reqeust):
    # api_key 노출되면 안되니까 git 같은 곳에 올리면 안되지 않을까
    # api_Key를 환경 변수로 빼내야 한다. 
    # 1. .env 파일을 생성하고 직접 read하도록 파이썬 코드 작성? -> 권장하지는 않는다
    # 2. django-environ 라이브러리 pip install django-environ
    # api_key 따로 빼내자.
    # project base에 .env 만들어서 api_key 넣기
    # settings.py BASE_DIR밑 import os, import environ ,,, 
    api_key = settings.API_KEY
    city_name = 'Seoul,KR'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
    response = requests.get(url).json()
    return Response(response)

@api_view(['GET'])
def save_data(request):
    # 1. API를 통해 데이터를 가져온다.
    api_key = settings.API_KEY
    city_name = 'Seoul,KR'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
    response = requests.get(url).json()

    # 2. 원하는 필드(dt_txt, temp, feels_like)만 꺼내서
    for li in response.get('list'):
        dt_txt = li.get('dt_txt')
        temp = li.get('main').get('temp')
        feels_like = li.get('main').get('feels_like')
        
        # 3. DB에 없다면 저장하기(중복된 건 빼기)
        # 저장하기 위해 데이터들을 포장해야한다.!
        # -> serializer로 변환하기
        # -> 유효성 검증, 저장 등 과정을 편하게 다룰 수 있다.

        # DB에 이미 저장되어 있는지 중복 확인
        if Weather.objects.filter(dt_txt=dt_txt, temp=temp, feels_like=feels_like).exists():
            continue

        save_data = {
            'dt_txt' : dt_txt,
            'temp': temp,
            'feels_like': feels_like,
        }

        serializer = WeatherSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    return JsonResponse({'message':'저장성공?'})

    
