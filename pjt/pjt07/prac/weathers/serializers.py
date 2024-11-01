from rest_framework import serializers
from .models import Weather

# serializer 왜 쓸까
# 우리가 제공하는 서비스는 웹서비스이므로 다른 언어, 환경에서 요청이 올수도 있다
# 모든 요청에서 부합할 수 있도록 데이터 형식을 정해야한다.
# 그래서 JSON 형식으로 돌려주자!
# DRF는 Json 형식으로 변환을 serializers를 통해서 쉽게 할 수 있도록 도와준다.
# DB에 저장된 필드들만 포장에 관여: ModelSerializer
# -> 여러 테이블의 데이터를 한 번에 포장: Nested Serializer
# DB 필드 외의 데이터들도 포장에 관여: Serializer

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'
    