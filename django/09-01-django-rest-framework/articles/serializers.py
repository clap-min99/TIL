from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields_ = '__all__'
        fields = ('id','title','content')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields_ = '__all__'
      