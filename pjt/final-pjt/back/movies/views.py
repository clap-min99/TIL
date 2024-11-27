from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.conf import settings
from .models import Movie, Beverage, Whiskey, Beer, Wine, NonAlcohol, Comment, MovieGenre
from .serializers import MovieSerializer, MovieListSerializer, BeverageSerializer, BeerSerializer, CommentSerializer, WhiskeySerializer, WineSerializer, NonAlcoholSerializer, GenreSerializer
import requests
# 검색관련 import
from django.db.models import Q



# Create your views here.

@api_view(['GET'])
def movie_all(request):
    movies = get_list_or_404(Movie)
    if request.method == 'GET':
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])  
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, movie_id = movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['GET'])
def movie_genre_list(request):
    genres = get_list_or_404(MovieGenre)
    if request.method == 'GET':
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_genre_detail(request, genre_id):
    genre = get_object_or_404(MovieGenre, id=genre_id)
    if request.method == 'GET':
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

@api_view(['GET'])
def beverage_main(request):
    beverages = get_list_or_404(Beverage)  
    if request.method == 'GET':
        serializer = BeverageSerializer(beverages, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def beer_list(request):
    beers = get_list_or_404(Beer)
    serializer = BeerSerializer(beers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def beer_detail(request, beer_id):
    beer = get_object_or_404(Beer, id=beer_id)
    serializer = BeerSerializer(beer)
    return Response(serializer.data)

@api_view(['GET'])
def whiskey_list(request):
    whiskies = get_list_or_404(Whiskey)
    serializer = WhiskeySerializer(whiskies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def whiskey_detail(request, whiskey_id):
    whiskey = get_object_or_404(Whiskey, id=whiskey_id)
    serializer = WhiskeySerializer(whiskey)
    return Response(serializer.data)

@api_view(['GET'])
def wine_list(request):
    wines = get_list_or_404(Wine)
    serializer = WineSerializer(wines, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def wine_detail(request, wine_id):
    wine = get_object_or_404(Wine, id=wine_id)
    serializer = WineSerializer(wine)
    return Response(serializer.data)

@api_view(['GET'])
def non_alcohol_list(request):
    nonalcohols = get_list_or_404(NonAlcohol)
    serializer = NonAlcoholSerializer(nonalcohols, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def non_alcohol_detail(request, non_alcohol_id):
    nonalcohol = get_object_or_404(NonAlcohol, id=non_alcohol_id)
    serializer = NonAlcoholSerializer(nonalcohol)
    return Response(serializer.data)

    
    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comment_list(request, movie_pk):
    if request.method == 'GET':
        comments = Comment.objects.filter(movie_id=movie_pk)  # 필터링 조건 예시
        print(comments)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, movie_id=movie_pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def comment_update(request, movie_pk, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id, movie_id=movie_pk)
        if request.user != comment.user:
            return Response({"detail": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Comment.DoesNotExist:
        return Response({"detail": "댓글을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, movie_pk, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id, movie_id=movie_pk)
        if request.user != comment.user:
            return Response({"detail": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        return Response({"detail": "댓글이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
    except Comment.DoesNotExist:
        return Response({"detail": "댓글을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

# 영화 검색

@api_view(['GET'])
def search_movies(request):
    query = request.GET.get('q', '')  # 쿼리 파라미터에서 검색어 가져오기
    if query:
        # 검색 조건: 제목, 줄거리, 배우, 감독에서 키워드가 포함된 경우
        movies = Movie.objects.filter(
            Q(title__icontains=query) | 
            Q(summary__icontains=query) | 
            Q(actors__icontains=query) | 
            Q(director__icontains=query)
        )
    else:
        movies = Movie.objects.all()  # 검색어가 없으면 전체 영화 반환
    serializer = MovieListSerializer(movies, many=True)  # 직렬화
    return Response(serializer.data)