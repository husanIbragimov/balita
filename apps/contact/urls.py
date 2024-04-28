from django.urls import path
from .views import get_in_touch

urlpatterns = [
    path('', get_in_touch, name="contact")
]