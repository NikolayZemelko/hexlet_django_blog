from django.views import View
from django.shortcuts import render


class ArticleIndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'articles/index.html', context={
            'article': 'About highest important things!',
        })
