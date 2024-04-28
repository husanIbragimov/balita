from .models import Article, Category, Tag

def data(request):
    categories = Category.objects.all().order_by('title')
    last_articles = Article.objects.all().order_by('-id')[:3]
    tags = Tag.objects.all().order_by('title')

    return {
       "categories": categories,
       "last_articles": last_articles,
       "tags": tags
    }
