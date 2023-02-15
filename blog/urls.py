from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView,SearchListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('searchresults',SearchListView.as_view(),name='search-results'),
    path('user/<username>',UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post/new/',PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),

    path('about/', views.about, name='blog-about')
]