from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse


class ArticleIndexView(View):

    def get(self, request, *args, **kwargs):
        return redirect(reverse('get_article_info', kwargs={
            'tag': 'python',
            'article_id': 42
        }))


def get_article(request, tag, article_id):
    return render(request, 'articles/article.html', context={
        'tag': tag,
        'article_id': article_id,
    })
