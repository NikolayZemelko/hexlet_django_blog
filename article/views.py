from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render, get_object_or_404, reverse

from .forms import CommentArticleForm
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
        comments = Comment.objects.filter(article__id=kwargs['id'])
        return render(request, 'articles/article.html', context={
            'article': article,
            'comments': comments,
        })

    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('article', kwargs={
            'id': kwargs['id'],
        }))
