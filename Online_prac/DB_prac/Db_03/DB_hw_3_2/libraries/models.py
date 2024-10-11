from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.TextField(max_length=50)
    age = models.IntegerField()
    birth = models.DateField()
    nationallity = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField()
    adult = models.BooleanField()
    price = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)