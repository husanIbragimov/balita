from django.db import models
from apps.account.models import Account
from django.template.defaultfilters import slugify  # new
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=225)
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title   


class Article(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=225)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # OneToMany
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    image_1 = models.ImageField(upload_to='Article/')
    image_2 = models.ImageField(upload_to='Article/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='Article/', null=True, blank=True)
    for_banner = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
        
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email
