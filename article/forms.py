from django.forms import ModelForm
from article.models import Comment


class CommentArticleForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']
