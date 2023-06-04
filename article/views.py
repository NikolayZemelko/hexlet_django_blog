from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render, get_object_or_404, reverse, redirect

from .forms import CommentArticleForm, ArticleForm
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


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles-index')

        return render(request, 'articles/create.html', {'form': form})
