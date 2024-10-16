from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookListSerializer, BookSerializer
from .models import Book
from django.shortcuts import render

# Create your views here.
@api_view(['GET','POST'])
def book_list(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE'])
def book_detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        book.delete()
        return Response({'delete' : f'도서 고유번호 {book.isbn}번의 {book.title}을 삭제하였습니다.'}, status=status.HTTP_204_NO_CONTENT)
    
    # elif request.method =='PUT':
    #     serializer = BookSerializer(book, data=request.data, partial = True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

