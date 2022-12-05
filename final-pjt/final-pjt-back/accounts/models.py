from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie, Review, Comment

# Create your models here.
class User(AbstractUser):
    img_path = models.ImageField(blank=True, null=True)
    backdrop_path = models.TextField(blank=True, null=True)
    like_movie = models.ManyToManyField(Movie, related_name='like_users')
    like_review = models.ManyToManyField(Review, related_name='like_users')
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    is_model = models.BooleanField(default=False)
    search_keyword_list = models.TextField(null=True)
    search_genres = models.TextField(null=True)
    search_production_companies = models.TextField(null=True)
    search_multi_keyword_list = models.TextField(null=True)
    search_multi_genres = models.TextField(null=True)
    search_multi_production_companies = models.TextField(null=True)
