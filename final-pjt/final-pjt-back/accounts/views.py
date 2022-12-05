from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from movies.serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import User
from django.contrib.auth import get_user_model
from movies.models import Genre, Movie, Review, Comment, Keyword, Production
from django.core.files.storage import default_storage

# from movies.serializers import LikeMoviesSerializer

import numpy as np
import pandas as pd
import requests
import ast
from random import choice

# Create your views here.


@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))	# 비밀번호 해싱(암호화)
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# profile
@api_view(['GET', 'POST'])
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    if request.method == 'GET':
        serializer = UserProfileSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = UserProfileSerializer(person, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view()
def like_movie(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    movies = person.like_movie.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view()
def write_review(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    reviews = person.review_set.all()
    movies = []
    for i in reviews.values():
        movie = Movie.objects.get(id=i['movie_id'])
        if movie not in movies:
            movies.append(movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    is_following = False
    if person != request.user:
        if request.method == "GET":
            if person.followers.filter(pk=request.user.pk).exists():
                is_following = True
            else:
                is_following = False
        elif request.method == "POST":
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
                is_following = False
            else:
                person.followers.add(request.user)
                is_following = True
    follower_count = person.followers.count()
    following_count = person.followings.count()
    data = {'follower_count':follower_count, 'following_count':following_count, 'is_following':is_following}
    return Response(data, status=status.HTTP_200_OK)


# 따로 쓰는거임
@api_view()
def like_movie_for_json(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    movies = person.like_movie.all()
    serializer = LikeMoviesSerializer(movies, many=True)
    return Response(serializer.data)



@api_view(['GET', 'POST'])
def analysis(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if request.method == 'GET':
        if person.is_model == True:
            if person.search_genres == '[]':
                search_genres = None
            else:
                search_genres = choice(ast.literal_eval(person.search_genres))
                dict_search_genres = Genre.objects.get(pk=search_genres)
                dict_search_genres = {dict_search_genres.name:dict_search_genres.id}
            
            if person.search_keyword_list == '[]':
                search_keyword_list = None
            else:
                search_keyword_list = choice(ast.literal_eval(person.search_keyword_list))
                dict_search_keyword_list = Keyword.objects.get(pk=search_keyword_list)
                dict_search_keyword_list = {dict_search_keyword_list.name:dict_search_keyword_list.id}
            
            if person.search_production_companies == '[]':
                search_production_companies = None
            else:
                search_production_companies=choice(ast.literal_eval(person.search_production_companies))
                dict_search_production_companies = Production.objects.get(pk=search_production_companies)
                dict_search_production_companies = {dict_search_production_companies.name:dict_search_production_companies.id}

            if person.search_multi_genres == '[]':
                dict_search_multi_genres = None
            else:
                search_multi_genres=choice(ast.literal_eval(person.search_multi_genres))
                dict_search_multi_genres = {}
                for genres_id in search_multi_genres:
                    tmp = Genre.objects.get(pk = genres_id)
                    dict_search_multi_genres[tmp.name] = tmp.id

            if person.search_multi_keyword_list == '[]':
                dict_search_multi_keyword_list = None
            else:
                search_multi_keyword_list=choice(ast.literal_eval(person.search_multi_keyword_list))
                dict_search_multi_keyword_list = {}
                for keyword_id in search_multi_keyword_list:
                    tmp = Keyword.objects.get(pk = keyword_id)
                    dict_search_multi_keyword_list[tmp.name] = tmp.id

            if person.search_multi_production_companies == '[]':
                dict_search_multi_production_companies = None
            else:
                search_multi_production_companies=choice(ast.literal_eval(person.search_multi_production_companies))
                dict_search_multi_production_companies = {}
                for production_id in search_multi_production_companies:
                    tmp = Production.objects.get(pk = production_id)
                    dict_search_multi_production_companies[tmp.name] = tmp.id


            data = {
                'is_model':person.is_model,
                'search_genres':dict_search_genres,
                'search_keyword_list':dict_search_keyword_list,
                'search_production_companies':dict_search_production_companies,
                'search_multi_genres':dict_search_multi_genres,
                'search_multi_keyword_list':dict_search_multi_keyword_list,
                'search_multi_production_companies':dict_search_multi_production_companies,
                }

            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                'is_model':person.is_model,
                }
            return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        movies = person.like_movie.all()
        keyword_list = []
        genres = []
        popularity = []
        production_companies = []
        vote_average = []
        for movie in movies:
            response = requests.get('https://api.themoviedb.org/3/movie/'+ str(movie.id) +'/keywords?api_key=94a2223b44d98108251e8243b8da5240&language=ko-KR')
            keyword_list.append(response.json()['keywords'])
            response = requests.get('https://api.themoviedb.org/3/movie/'+ str(movie.id) +'?api_key=94a2223b44d98108251e8243b8da5240&language=ko-KR')
            genres.append(response.json()['genres'])
            popularity.append(response.json()['popularity'])
            production_companies.append(response.json()['production_companies'])
            vote_average.append(response.json()['vote_average'])

        movie_popularity = pd.DataFrame(popularity)
        movie_vote_average = pd.DataFrame(vote_average)

        keyword_list_dict = {}
        using_keyword = {}
        for i in keyword_list:
            for j in i:
                if j['id'] not in keyword_list_dict:
                    keyword_list_dict[j['id']] = 1
                    using_keyword[j['id']] = j['name']
                else:
                    keyword_list_dict[j['id']]+= 1
        df_keyword_list = pd.DataFrame(keyword_list_dict, index=['count'])

        genres_dict = {}
        using_genres = {}
        for i in genres:
            for j in i:
                if j['id'] not in genres_dict:
                    genres_dict[j['id']] = 1
                    using_genres[j['id']] = j['name']
                else:
                    genres_dict[j['id']]+= 1
        df_genres = pd.DataFrame(genres_dict, index=['count'])

        production_companies_dict = {}
        using_production_companies = {}
        for i in production_companies:
            for j in i:
                if j['id'] not in production_companies_dict:
                    production_companies_dict[j['id']] = 1
                    using_production_companies[j['id']] = j['name']
                else:
                    production_companies_dict[j['id']]+= 1
        df_production_companies = pd.DataFrame(production_companies_dict, index=['count'])
        
        movie_keyword_list = pd.DataFrame([])
        for i in keyword_list:
            keyword_list_dict = pd.DataFrame([])
            for j in i:
                keyword_list_dict[j['id']] = [1]
            movie_keyword_list = pd.concat((movie_keyword_list, keyword_list_dict))
        movie_keyword_list= movie_keyword_list.fillna(0)
        movie_keyword_list = movie_keyword_list.astype('int')  
        
        movie_genres = pd.DataFrame([], columns=using_genres.keys())
        for i in genres:
            genres_dict = pd.DataFrame([])
            for j in i:
                genres_dict[j['id']] = [1]
            movie_genres = pd.concat((movie_genres, genres_dict))
        movie_genres= movie_genres.fillna(0)
        movie_genres = movie_genres.astype('int')
        
        movie_production_companies = pd.DataFrame([])
        for i in production_companies:
            production_companies_dict = pd.DataFrame([])
            for j in i:
                production_companies_dict[j['id']] = [1]
            movie_production_companies = pd.concat((movie_production_companies, production_companies_dict))
        movie_production_companies= movie_production_companies.fillna(0)
        movie_production_companies = movie_production_companies.astype('int')
        
        movie_keyword_list_corr=movie_keyword_list.corr()
        movie_genres_corr = movie_genres.corr()
        movie_production_companies_corr = movie_production_companies.corr()
        
        search_keyword_list = list(df_keyword_list.T.sort_values(by='count' ,ascending=False).head(5).index)
        search_genres = list(df_genres.T.sort_values(by='count' ,ascending=False).head(5).index)
        search_production_companies = list(df_production_companies.T.sort_values(by='count',ascending=False).head(5).index)
        
        search_multi_keyword_list = []
        for i in search_keyword_list:
            tmp = list(movie_keyword_list_corr[i].sort_values(ascending=False).index)
            if len(tmp) > 5:
                search_multi_keyword_list.append(tmp[:4])
            else:
                search_keyword_list.append(tmp[:])

        search_multi_genres = []
        for i in search_genres:
            tmp = list(list(movie_genres_corr[i].sort_values(ascending=False).index))
            if len(tmp) > 3:
                search_multi_genres.append(tmp[:2])
            else:
                search_multi_genres.append(tmp[:])

        search_multi_production_companies = []
        for i in search_production_companies:
            tmp = list(movie_production_companies_corr[i].sort_values(ascending=False)[:4].index)
            if len(tmp) > 5:
                search_multi_production_companies.append(tmp[:4])
            else:
                search_multi_production_companies.append(tmp[:])

        person.is_model = True
        person.search_keyword_list = search_keyword_list
        person.search_genres = search_genres
        person.search_production_companies = search_production_companies
        person.search_multi_keyword_list = search_multi_keyword_list
        person.search_multi_genres = search_multi_genres
        person.search_multi_production_companies = search_multi_production_companies
        person.save()

        for key, value in using_keyword.items():
            try:
                Keyword.objects.get(pk=key)
            except:
                keyword = Keyword()
                keyword.pk = key
                keyword.name = value
                keyword.save()
    
        for key, value in using_production_companies.items():
            
            try:
                Production.objects.get(pk=key)
            except:
                production = Production()
                production.pk = key
                production.name = value
                production.save()
        print(using_genres)
        for key, value in using_genres.items():
            try:
                Genre.objects.get(pk=key)
            except:
                genre = Genre()
                genre.pk = key
                genre.name = value
                genre.save()

        return Response(status=status.HTTP_201_CREATED)
