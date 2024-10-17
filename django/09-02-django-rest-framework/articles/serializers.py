from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
        )


class ArticleSerializer(serializers.ModelSerializer):
    # article 입장에서 comment는 다중데이터 -> many=True
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id','content',)
    
    # comment_set 역참조 데이터를 override
    comment_set = CommentDetailSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # source는 필드를 채우는데 사용할 속성 이름
    # 점 표기법을 사용해 속성 탐색 comment_set.count

    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    
    # 기존 article 데이터 값을 override
    # 기존 fielld를 override 하게도ㅣ면 Meta class의 read_only_fields를 사용할 수 없다.
    article= ArticleTitleSerializer(read_only=True)
           
    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)
        # 외래키 데이터는 유효성 검사에서는 제외하고
        # 결과 데이터에는 포함하고 싶다
        # 그래서 읽기 전용 필드로 지정해야한다!(read_only_fields)
        # but 특정 필드를 override or 추가한 경우 
        # read_only_fields 는 동작하지 않는다. 
        # 그래서 새로운 필드에 read_only 키워드 인자로 작성해야함