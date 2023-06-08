from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render, get_object_or_404, reverse, redirect

from .forms import CommentArticleForm, ArticleForm
from article.models import Article, Comment
from django.contrib import messages


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
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


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):

        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)

        return render(request, 'articles/update.html', {'form': form,
                                                        'article_id': article_id
                                                        })

    def post(self, request, *args, **kwargs):

        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Article is updated.')
            return redirect('articles-index')

        return render(request, 'articles/update.html', {'form': form,
                                                        'article_id': article_id
                                                        })
