from django.shortcuts import render
from .models import Movie, Review, Comment
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import MovieListSerializer, MovieSerializer, ReviewSerializer, CommentSerializer
from django.contrib.auth import get_user_model


# Create your views here.

# movies
@api_view(['GET'])
def get_movies(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def like_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == "GET":
        if movie.like_users.filter(pk=request.user.pk).exists():
            is_movie_like = True
        else:
            is_movie_like = False
    elif request.method == "POST":
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
            is_movie_like = False
        else:
            movie.like_users.add(request.user)
            is_movie_like = True
    movie_like_count = movie.like_users.count()
    data = {'movie_like_count':movie_like_count, 'is_movie_like':is_movie_like}
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_our_rating(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    reviews = movie.review_set.all()
    review_count = reviews.count()
    if reviews:   
        sumV = 0
        for i in reviews.all():
            sumV += i.rating
        our_rating = sumV/review_count
    else:
        our_rating = 0
    data = {'our_rating':round(our_rating, 2), 'review_count':review_count}
    return Response(data, status=status.HTTP_200_OK)


# reviews
@api_view(['GET', 'POST'])
def get_or_create_reviews(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == 'GET':
        reviews = Review.objects.filter(movie_id=movie_id)
        serializer = ReviewSerializer(reviews, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def update_or_delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def like_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    if request.method == "GET":
        if review.like_users.filter(pk=request.user.pk).exists():
            is_review_like = True
        else:
            is_review_like = False
    elif request.method == "POST":
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
            is_review_like = False
        else:
            review.like_users.add(request.user)
            is_review_like = True
    review_like_count = review.like_users.count()
    data = {'review_like_count':review_like_count, 'is_review_like':is_review_like}
    return Response(data, status=status.HTTP_200_OK)


# comments
@api_view(['GET', 'POST'])
def get_or_create_comments(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'GET':
        comments = Comment.objects.filter(review_id=review_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def update_or_delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def search(request):
    keyword = request.data['keyword']
    movies = Movie.objects.filter(title__contains=keyword)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

