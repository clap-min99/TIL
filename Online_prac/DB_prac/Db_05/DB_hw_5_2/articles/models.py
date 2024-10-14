# articles/models.py
from django.db import models
from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 상대방이든 나읻느 역참조 명이 중복되는 경우가 발생하면
    # 기능적으로 불가능해지므로 이러한 상황에 대해서만 특별히 
    # 역참조 매니저명(related_name)을 별도로 지정해줘야한다.!
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name = 'like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

'''
환자랑 의사가 1:N의 관계이면서 
의사랑 환자가 1:N의 관계가 되도록 하면 되지 않을까?

대신, 마구잡이로 1:N의 관계를 데이터베이스 설정할 때 만들면,
1. 컬럼이 너무 복잡해진다.
2. 의사랑 환자가 1:N의 관계를 맺는 경우가 하나가 아니라 여러개가 될 경우, 
헷갈리는 경우도 너무 많다. 
3. 그래서 의사(1): 환자(N)와 환자(1):의사(N)은 사실 서로 다른 관계가 아니라 결국 진료라는 하나의 관계인데
컬럼은 두 개가 만들어진다. 
'''

