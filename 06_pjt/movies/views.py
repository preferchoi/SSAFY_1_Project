from urllib import request
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Movie, Comment
# from .forms import MovieForm, CommentForm



# Create your views here.
# 전체 페이지 조회
def index(request):
    movies = Movie.objects.order_by("-pk")

    context = {
        "movies": movies,
    }
    return render(request, "movies/index.html", context)

# 새로운 영화 생성 페이지 조회, 단일 영화 데이터 저장
def create(request):
    pass

# 단일 영화 상세 페이지
def detail(request):
    pass

# 기존 영화 수정 페이지 조회, 단일 영화 데이터 수정
def update(request):
    pass

# 단일 영화 데이터 삭제
def delete(request):
    pass

# 단일 댓글 데이터 저장
def comments(request):
    pass

# 단일 댓글 데이터 삭제
def comment_delete(request):
    pass



  