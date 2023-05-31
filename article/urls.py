from django.urls import path
from article import views

urlpatterns = [
    path('', views.ArticleIndexView.as_view(), name='articles-index'),
    path('<str:tag>/<int:article_id>/', views.article, name='article'),
]
