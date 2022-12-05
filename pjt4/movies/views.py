from django.shortcuts import render, redirect

from movies.models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'index.html', context)


def new(request):

    context = {
        
    }
    
    return render(request, 'new.html', context)


def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_data = request.POST.get('release_data')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    movie = Movie(title=title,audience=audience,release_data=release_data,genre=genre,score=score,poster_url=poster_url,description=description)
    movie.save()
    return redirect('movies:index')


def detail(request, pk):
    movie = Movie.objects.get(pk = pk)
    context = {
        'movie':movie        
    }
    
    return render(request, 'detail.html', context)


def edit(request, pk):
    movie = Movie.objects.get(pk = pk)
    context = {
        'movie':movie        
    }
    
    return render(request, 'edit.html', context)


def update(request, pk):
    movie = Movie.objects.get(pk = pk)
    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.release_data = request.POST.get('release_data')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.save()
    
    return redirect('movies:detail', movie.pk)


def delete(request, pk):
    movie = Movie.objects.get(pk = pk)
    movie.delete()
    
    return redirect('movies:index')