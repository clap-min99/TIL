from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form' : form
    }
    return render(request, 'movies/create.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comments = movie.comment_set.all()
    comment_form = CommentForm()
    context = {
        'movie' : movie,
        'comments' : comments,
        'comment_form': comment_form,
    }
    return render(request, 'movies/detail.html', context)

@login_required    
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance = movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie' : movie,
        'form' : form,
    }
    return render(request, 'movies/update.html', context)

@login_required
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')

@login_required
def comments_create(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()
        return redirect('movies:detail', movie.pk)
    context = {
        'movie' :  movie,
        'comment_form' : comment_form,
    }
    return render(request, 'movies/detail.html', context)

@login_required
def comments_delete(request, movie_pk, comment_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment = Comment.objects.get(pk=comment_pk)

    if request.user == comment.user:
        comment.delete()
    return redirect('movies:detail', movie.pk)


@login_required
def likes(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)

    return redirect('movies:index')