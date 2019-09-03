from django.urls import path

from .views import *

app_name = 'webapp'

urlpatterns = [
    path('', post_views.IndexView.as_view(), name='index'),
    path('posts/<int:pk>', post_views.PostDetailView.as_view(), name='post_detail'),
    path('posts/create', post_views.PostCreateView.as_view(), name='post_create'),
    ]