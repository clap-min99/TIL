from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 작성자 정보
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1

    )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name ='like_movies')


class Comment(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    content = models.CharField(max_length=300)