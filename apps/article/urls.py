from django.urls import path
from .views import index, article_detail, category_view

urlpatterns = [
    path('', index),
    path('detail/<int:pk>/', article_detail, name="detail"),
    path('category/<int:cat_pk>/', category_view, name="category")
]