from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse

from article.models import Article


class ArticleIndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


def article(request, tag, article_id):
    return render(request, 'articles/article.html', context={
        'tag': tag,
        'article_id': article_id,
    })
