from django.shortcuts import render
from .models import Article, Category, Tag
from django.core.paginator import Paginator


def index(request):
    tag = request.GET.get('tag')

    articles = Article.objects.all().order_by('-id')
    categories = Category.objects.all().order_by('title')
    tags = Tag.objects.all().order_by('title')
    banners = articles.filter(for_banner=True)
    last_articles = articles.all()[:3]

    if tag:
        articles = articles.filter(tags__title__exact=tag)

    page_number = request.GET.get('page')
    paginator = Paginator(articles, 10)
    selected_page = paginator.get_page(page_number)
    selected_page.adjusted_elided_pages = paginator.get_elided_page_range(page_number)

    context = {
        "articles": selected_page,
        "categories": categories,
        "tags": tags,
        "banners": banners,
        "last_articles": last_articles
    }
    return render(request, 'index.html', context)


def article_detail(request, pk):
    article = Article.objects.get(id=pk)

    context = {
        "article": article
    }

    return render(request, 'blog-single.html', context)
