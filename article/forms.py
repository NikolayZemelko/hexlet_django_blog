from django.forms import ModelForm
from article.models import Comment, Article


class CommentArticleForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
