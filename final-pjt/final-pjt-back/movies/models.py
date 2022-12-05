from django.db import models
from django.conf import settings


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50, null=False)


class Keyword(models.Model):
    name = models.CharField(max_length=50, null=False)


class Production(models.Model):
    name = models.CharField(max_length=100, null=False)
    

class Movie(models.Model):
    title = models.CharField(max_length=50, null=False)
    vote_average = models.FloatField(null=False)
    popularity = models.FloatField(null=False)
    overview = models.TextField()
    released_date = models.CharField(max_length=10, null=False)
    poster_path = models.CharField(max_length=200, null=False)
    backdrop_path = models.CharField(max_length=200, default='', null=True)
    genres = models.ManyToManyField(Genre)
   
    
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(null=False)
    rating = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField(null=False)


