from django.urls import path

from .views import *

app_name = 'webapp'

urlpatterns = [
    path('', post_views.IndexView.as_view(), name='index'),
    path('posts/<int:pk>', post_views.PostDetailView.as_view(), name='post_detail'),
    path('posts/create', post_views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/comment_create', comment_views.CommentCreateView.as_view(), name='comment_create'),
    path('posts/<int:pk>/like', post_views.put_likes, name='put_likes'),
    path('search', search_views.SearchView.as_view(), name='search')
]
