"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views

urlpatterns = [
    path("", include("register.urls")),
    path("login/", include("login.urls")),
    path('admin/', admin.site.urls),
    path("user/", include("reaction.urls")),
    path('calculator/', include("calculator.urls")),
    path('logout', views.LogoutView.as_view(), name = "logout")
    
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
