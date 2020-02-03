from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    my_title = "Hello Marline"
    return render(request, "home.html", {"title": my_title})


def about_page(request):
    return render(request, "home.html", {"title": "About us"})


def contact_page(request):
    return render(request, "home.html", {"title": "Contact us"})
