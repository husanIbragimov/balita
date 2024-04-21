from django.urls import path
from .views import index, article_detail

urlpatterns = [
    path('', index),
    path('detail/<int:pk>/', article_detail, name="detail")
]