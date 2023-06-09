from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp')
    search_fields = ['name', 'body']
    list_filter = (('timestamp', DateFieldListFilter),)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'timestamp')
    search_fields = ['name', 'content']
    list_filter = (('timestamp', DateFieldListFilter),)
