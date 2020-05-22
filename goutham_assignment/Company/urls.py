from django.urls import path
from .views import PostDetailView, PostCreateView


urlpatterns = [
    path('<int:pk>/', PostDetailView.as_view(), name='company'),
    path('create/', PostCreateView.as_view(), name='company_create'),
]
