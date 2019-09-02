from django.urls import path

from .views import *

app_name = 'webapp'

urlpatterns = [
    path('', post_views.IndexView.as_view(), name='index'),
    ]