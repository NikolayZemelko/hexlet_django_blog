from django.urls import path
from article import views

urlpatterns = [
    path('', views.ArticleIndexView.as_view(), name='article'),
    path('<str:tag>/<int:article_id>/', views.get_article, name='get_article_info'),
]
