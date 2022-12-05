from rest_framework import serializers
from .models import Movie, Review, Comment, Genre


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ('user', 'review',)


class ReviewSerializer(serializers.ModelSerializer):
    
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    class Meta:
        model = Review
        fields = ('id', 'user', 'username', 'movie', 'title', 'content', 'rating',)
        read_only_fields = ('id', 'user', 'movie',)


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "poster_path", "backdrop_path",)


class LikeMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'vote_average', 'genres', 'popularity')



class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"

