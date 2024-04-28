from django.shortcuts import render, redirect
from .models import GetInTouch
from .forms import GetInTouchForm


def get_in_touch(request):
    form = GetInTouchForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("contact")
    
    return render(request, "contact.html", {"form": form})