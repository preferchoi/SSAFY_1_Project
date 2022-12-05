from .models import Movie
from community.models import Review
from accounts.models import User
from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth import get_user_model




# Create your views here.
@require_safe
@require_http_methods(['GET'])
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)



@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)
    


@require_safe
def recommended(request):
    if request.user.is_authenticated:
        person = request.user
        # print(person) => user02
        # review = Review.objects.all().filter(user = person)
        # print(review) => 내가 작성한 리뷰들
        
        targets = []
        users = User.objects.all()
        for user in users:
            if user.followers.filter(pk=person.pk):
                targets.append(user)
        # print(targets) # => 내가 팔로우한 유저들

        target_movie_title = []
        for i in targets:
            review = Review.objects.get(user = i)
            target_movie_title.append(review.movie_title)
        # print(target_movie_title) => 리뷰 영화 제목
        
        target_genres = set()
        for i in target_movie_title:
            movie = Movie.objects.get(title = i)
            for i in movie.genres.all():
                target_genres.add(i)
        # print(target_genres) => 장르 pk
        movie_lst = set()
        for i in target_genres:
            movies = Movie.objects.all()
            for movie in movies:
                for m_g in movie.genres.all():
                    if m_g == i:
                        movie_lst.add(movie)

        sorted_movie_lst = []
        for i in movie_lst:
            sorted_movie_lst.append([i.pk, i.vote_average])
        sorted_movie_lst.sort(key=lambda x:x[1], reverse=True)
        # print(sorted_movie_lst)
        return_lst = []
        for i_pk, i_avg in sorted_movie_lst[:10]:
            return_lst.append(Movie.objects.get(pk=i_pk))
        context = {
            'movies': return_lst
        }
        return render(request, 'movies/index.html', context)
    return render(request, 'accounts/login.html', context)
