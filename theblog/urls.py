from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, AddCommentView
from .import views

urlpatterns = [
    #path("", views.home, name="home"),
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    path("add_post/", AddPostView.as_view(), name="add_post"),
    path("article/edit/<int:pk>", UpdatePostView.as_view(), name="update_post"),
    path("article/<int:pk>/remove", DeletePostView.as_view(), name="delete_post"),
    path("add_category/", AddCategoryView.as_view(), name="add_category"),
    #path("category/<int:i>", views.category_view, name="category"),
    path("category/<str:i>", views.category_view, name="category"),
    path("likes/<int:pk>", views.like_view, name='like_post'),
    path("artilce/<int:pk>/comment", AddCommentView.as_view(), name="add_comment"),
]