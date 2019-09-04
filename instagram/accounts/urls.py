from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import register_view, UserDetailView, UserPersonalInfoChangeView, subscribe_to_user

app_name = 'accounts'

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('create/', register_view, name='create'),
    path('<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/update', UserPersonalInfoChangeView.as_view(), name='user_update'),
    path('<int:pk>/subscribe', subscribe_to_user, name='subscribe_to_user'),
]
