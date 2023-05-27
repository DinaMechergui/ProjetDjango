from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article_detail.html', {'article': article})