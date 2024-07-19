from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import UserLogin, UserPasswordChange, UserRegister, UserProfile

app_name = 'user'

urlpatterns = [
    # path('register/', UserRegister.as_view(), name='register'),
    path('profile/', UserProfile.as_view(), name='profile'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', UserPasswordChange.as_view(), name='password_change'),
]
