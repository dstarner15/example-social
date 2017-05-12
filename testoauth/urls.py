"""testoauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def tony_view(request):
    return render(request, "tony.html")

def tony_view2(request):
    return render(request, "tony2.html")

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^admin/', admin.site.urls),
    url('', include('social_django.urls', namespace='social')),
    url(r'^tony2', tony_view2, name='tony2'),
    url(r'^tony1', tony_view, name='tony')
]
