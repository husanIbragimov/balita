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
    more_articeles = articles.all().order_by('?')[:4]

    if tag:
        articles = articles.filter(tags__title__exact=tag)

    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    selected_page = paginator.get_page(page_number)
    selected_page.adjusted_elided_pages = paginator.get_elided_page_range(page_number)

    context = {
        "articles": selected_page,
        "categories": categories,
        "tags": tags,
        "banners": banners,
        "last_articles": last_articles,
        "more_articles": more_articeles
    }
    return render(request, 'index.html', context)


def article_detail(request, pk):
    article = Article.objects.get(id=pk)

    articles = Article.objects.filter(category_id=article.category.id)[:3]
    context = {
        "article": article,
        "articles": articles
    }

    return render(request, 'blog-single.html', context)


def category_view(request, cat_pk):
    page_number = request.GET.get('page')
    category = Category.objects.get(id=cat_pk)
    articles = Article.objects.filter(category_id=cat_pk).order_by('-created_at')

    paginator = Paginator(articles, 1)
    selected_page = paginator.get_page(page_number)

    context = {
        "articles": selected_page,
        "category": category
    }

    return render(request, 'category.html', context)