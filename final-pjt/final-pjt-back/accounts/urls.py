from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # jwt
    path('signup/', views.signup, name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # profile
    path('profile/<username>/', views.profile, name = 'profile'),
    path('<int:user_pk>/like_movie/', views.like_movie, name='like_movie'),
    path('<int:user_pk>/write_review/', views.write_review, name='write_review'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),

    # path('<int:from_user_pk>/follow/<int:to_user_pk>/', views.follow2, name='follow2'),
    path('<int:user_pk>/like_movie_for_json/', views.like_movie_for_json, name='like_movie_for_json'),
    path('profile/<int:user_pk>/analysis/', views.analysis, name='analysis'),
]
