from rest_framework import serializers
from movies.models import Movie
from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # 반환되지않도록함

    class Meta:
        model = get_user_model()
        fields = ('username', 'password',)

class UserProfileSerializer(serializers.ModelSerializer):
    img_path = serializers.ImageField(required=False)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'img_path', 'backdrop_path')
        read_only_fields = ('username',)


class UserAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'is_model', 'search_keyword_list', 'search_genres', 'search_production_companies', 'search_multi_keyword_list', 'search_multi_genres', 'search_multi_production_companies',)