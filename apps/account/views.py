from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Account


def register_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        avatar = request.FILES.get('avatar')
        password = request.POST.get('password')

        if Account.objects.filter(username=username).exists():
            raise ValueError("Username already exists!")
        
        user = Account.objects.create_user(
            first_name=full_name,
            username=username,
            email=email,
            avatar=avatar,
            password=password,
        )

        login(request, user)
        return redirect("/")
    
    return render(request, 'register.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(user)
        login(request, user)
        return redirect("/")
    
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect("/")