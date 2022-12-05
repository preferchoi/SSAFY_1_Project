from django.urls import path
from . import views


urlpatterns = [
    path('actor_list/', views.actor_list),
    path('actor_detail/<int:actor_pk>/', views.actor_detail),
    path('movie_list/', views.movie_list),
    path('movie_detail/<int:movie_pk>/', views.movie_detail),
    path('review_list/', views.review_list),
    path('review_detail/<int:review_pk>/', views.review_datail),
    path('movie_detail/<int:movie_pk>/create_review/', views.create_review),
]