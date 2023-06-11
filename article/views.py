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
        article_id = kwargs.get('id')
        article = get_object_or_404(Article, id=article_id)
        form = CommentArticleForm()
        comments = Comment.objects.filter(article_id=article_id)
        return render(request, 'articles/article.html', context={
            'article': article,
            'comments': comments,
            'form': form
        })

    def post(self, request, *args, **kwargs):

        article_id = kwargs.get('id')
        form = CommentArticleForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.name = form.cleaned_data['name']
            comment.content = form.cleaned_data['content']
            comment.article_id = Article.objects.get(id=article_id)
            comment.save()
            return redirect('article', id=article_id)

        return HttpResponseRedirect(reverse('article', kwargs={
            'id': article_id,
        }))


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form
                                                        })

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles-index')

        return render(request, 'articles/create.html', {'form': form
                                                        })


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


class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):

        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)

        if article:
            article.delete()
            messages.add_message(request, messages.INFO, 'Article is deleted.')
        return redirect('articles-index')
