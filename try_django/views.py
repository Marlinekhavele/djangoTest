from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    my_title = "Hello Marline"
    context = {"title": my_title}
    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html", {"title": "About"})


def contact_page(request):
    return render(request, "home.html", {"title": "Contact us"})

