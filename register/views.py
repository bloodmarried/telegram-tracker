from django.shortcuts import render, redirect
from django.http import HttpRequest
from django_telegram_login.authentication import verify_telegram_authentication

# Create your views here.

def register(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("user", request.user.reviews.user_id)
    return render(request, "register/index.html")