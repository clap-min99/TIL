from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
    # 전체 게시글 조회(type:queryset, queryset은 장고에서 쓰는 데이터타입)
        articles = Article.objects.all()
        # 변환하기 쉬운 포멧으로 전환(직렬화)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        # 유효성 검사
        if serializer.is_valid():
            serializer.save()
            # 저장 성공 후 201 응답 상태코드 반환
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        




@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)