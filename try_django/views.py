from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render("home.html")


def about_page(request):
    return HttpResponse("<h1>Hello about</h1>")


def contact_page(request):
    return HttpResponse("<h1>Hello contact</h1>")
