from django.shortcuts import redirect, render
from django.urls import is_valid_path

from .forms import MovieForm
from .models import Movie
# Create your views here.

# 전체 영화 데이터 조회 및 index.html 렌더링
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)


# create.html 렌더링, 유효성 검증 및 영화 데이터 저장 후 detail.html 리다이렉트
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form':form,
    }
    return render(request, 'movies/create.html', context)


# 단일 영화 데이터 조회 및 detail.html 렌더링
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


# 수정 대상 영화 데이터 조회 및 update.html 렌더링
# 유효성 검증 및 영화 데이터 수정 후 detail.html 리다이렉트
def update(request, pk):
    movie = Movie.objects.get(pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)

    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)


# 단일 영화 데이터 삭제 및 index.html 리다이렉트
def delete(request, pk):
    return render(request, 'movies/index.html')
