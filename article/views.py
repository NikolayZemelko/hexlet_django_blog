from django.views import View
from django.shortcuts import render, get_object_or_404

from article.models import Article, Comment


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/article.html', context={
            'article': article,
        })


class ArticleCommentsView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['article_id'])
        comments = Comment.objects.filter(article__id=kwargs['article_id'])
        return render(request, 'articles/comment.html', context={
            'comments': comments,
            'article': article,
        })
