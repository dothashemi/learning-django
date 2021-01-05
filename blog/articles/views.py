from django.shortcuts import render
from .models import Article


def index(request):
    articles = Article.objects.order_by("-published")[:10]
    
    return render(request, 'index.html', {
        'title': 'Articles Page',
        'articles': articles
    })


def show(request, id):
    article = Article.objects.get(id=id)

    return render(request, 'show.html', {
        'title': article.title,
        'article': article
    })
