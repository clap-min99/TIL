from django.shortcuts import render
from .models import Author

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context ={
        'authors':authors,
    }
    return render(request, 'libraries/index.html', context)


def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    context = {
        'author': author
    }
    return render(request, 'libraries/detail.html', context)