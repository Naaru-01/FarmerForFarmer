from django.urls import path
from django.conf.urls import url, include

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    AddCommentView,


)
from . import views

urlpatterns = [
    path('experiences/', PostListView.as_view(), name='blog-experience'),
    path('answers/', AddCommentView.as_view(), name='add-comment'),

    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('', views.home1, name='blog-home1'),
    
   

]
