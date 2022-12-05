from django.urls import path
from . import views

urlpatterns = [
    # movies
    path('', views.get_movies , name='get_movies'),
    path('<int:movie_id>/', views.get_movie, name='get_movie'),
    path('<int:movie_id>/like_movie/', views.like_movie, name='like_movie'),
    path("<int:movie_id>/get_our_rating/", views.get_our_rating, name="get_our_rating"),
    
    # reviews
    path('<int:movie_id>/reviews/', views.get_or_create_reviews, name='get_or_create_reviews'), 
    path('reviews/<int:review_id>/', views.update_or_delete_review, name='update_or_delete_review'),
    path('<int:review_id>/like_review/', views.like_review, name='like_review'),
    
    # comments
    path("<int:review_id>/comments/", views.get_or_create_comments, name="get_or_create_comments"),
    path('comments/<int:comment_id>/', views.update_or_delete_comment, name='update_or_delete_comment'),

    # search
    path('search/', views.search, name='search'),
]   
