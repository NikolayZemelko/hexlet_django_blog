from django.urls import path
from article.views import ArticleIndexView

urlpatterns = [
    path('', ArticleIndexView.as_view()),
]
