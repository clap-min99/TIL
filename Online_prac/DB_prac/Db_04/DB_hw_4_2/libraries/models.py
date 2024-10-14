from django.db import models
from django.conf import settings

# Create your models here.

class Book(models.Model):
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=200)

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)