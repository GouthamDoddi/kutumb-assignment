from django.urls import path
from .views import register, profile
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', register, name='register'),
    # below are default django inbuilt views

    path('login/', auth_views.LoginView.as_view(template_name='Profile/login.html'),
         name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='Profile/logout.html'),
         name='logout'),
    # profile url

    path('profile/', profile, name='profile'),
]
