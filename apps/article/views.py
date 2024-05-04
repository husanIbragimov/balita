from django.shortcuts import render, redirect
from .models import Article, Category, Comment
from django.core.paginator import Paginator


def index(request):
    tag = request.GET.get('tag')
    articles = Article.objects.all().order_by('-id')
    banners = articles.filter(for_banner=True)
    more_articeles = articles.all().order_by('?')[:4]

    if tag:
        articles = articles.filter(tags__title__exact=tag)

    page_number = request.GET.get('page')
    paginator = Paginator(articles, 10)
    selected_page = paginator.get_page(page_number)
    selected_page.adjusted_elided_pages = paginator.get_elided_page_range(page_number)

    context = {
        "articles": selected_page,
        "banners": banners,
        "more_articles": more_articeles
    }
    return render(request, 'index.html', context)


def article_detail(request, slug):
    article = Article.objects.get(slug__exact=slug)

    articles = Article.objects.filter(category_id=article.category.id)[:3]
    comments = Comment.objects.filter(article_id=article.id)

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("comment")
        
        Comment.objects.create(
            article_id=article.id,
            user=request.user,
            name=name,
            email=email,
            comment=comment
        )
        return redirect('detail', article.slug)
        

    context = {
        "article": article,
        "articles": articles,
        "comments": comments
    }

    return render(request, 'blog-single.html', context)


def category_view(request, slug):
    page_number = request.GET.get('page')
    tag = request.GET.get('tag')
    category = Category.objects.get(slug__exact=slug)
    articles = Article.objects.filter(category__slug__exact=slug).order_by('-created_at')

    if tag:
        articles = articles.filter(tags__title__exact=tag)

    paginator = Paginator(articles, 10)
    selected_page = paginator.get_page(page_number)

    context = {
        "articles": selected_page,
        "category": category
    }

    return render(request, 'category.html', context)