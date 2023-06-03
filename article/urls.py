from django.urls import path
from article import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles-index'),
    path('<int:id>/', views.ArticleView.as_view(), name='article'),
    path('<int:article_id>/comments/', views.ArticleCommentsView.as_view(), name='comments'),
]
