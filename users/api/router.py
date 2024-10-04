from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from users.api.views import RegisterView, UserView, UserListView, CustomTokenObtainPairView, LogOutView

urlpatterns = [
    path('auth/register', RegisterView.as_view()),
    path('auth/me', UserView.as_view()),
    path('auth/all', UserListView.as_view()),
    path('auth/login', CustomTokenObtainPairView.as_view()),
    path('auth/logout', LogOutView.as_view()),
    path('auth/token/refresh', TokenRefreshView.as_view())
]