from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.conf import settings
from django_telegram_login.authentication import verify_telegram_authentication
from django_telegram_login.errors import NotTelegramDataError, TelegramDataIsOutdatedError
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from reaction.models import Reviews
from django.utils import timezone
import datetime

# Create your views here.

bot_token = settings.TELEGRAM_BOT_TOKEN


def login_system(request: HttpRequest):
    
    if not request.GET.get('hash'):
        return HttpResponse('Handle the missing Telegram data in the response.')
    
    try:
        
        result = verify_telegram_authentication(bot_token, request.GET)
        user_info = Reviews.objects.filter(user_id = result["id"]).first()
        if user_info:
            user = User.objects.get(username = result["username"])
            login(request, user)
            return redirect("user", result["id"])
        print(result)
        time = timezone.make_aware(datetime.datetime.fromtimestamp(int(result["auth_date"])))
        user = User.objects.create_user(username = result["username"], first_name = result["first_name"], date_joined = time)
        new_reviws = Reviews(user_id = result["id"], picture = result["photo_url"], username = user, date = time)
        new_reviws.save()
        login(request, user)
        return redirect("user", result["id"])
        
    except NotTelegramDataError:
        return HttpResponse('The data is not related to Telegram!')
    except TelegramDataIsOutdatedError:
        return HttpResponse('Authentication was received more than a day ago.')
    
    
    
    