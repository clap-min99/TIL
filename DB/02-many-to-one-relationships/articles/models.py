from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # ariticle에 대한 외래 키
    # 외래키는 참조하려는 변수의 단수로 한다.
    # ForeignKey(상대모델클래스, 상대 모델 클래스가 삭제 되었을 때 댓글을 어떻게 처리할 지)
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
