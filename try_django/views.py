from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from blog.models import BlogPost


def home_page(request):
    my_title = "Hello Marline"
    qs = BlogPost.objects.all()[:5]
    context = {"title": "Welcome", "blog_list": qs}
    # if request.user.is_authenticated:
    #     context = {"title": my_title, "my_list": [1, 2, 3, 4, 5, 6, 7, 8, 9]}
    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html", {"title": "About"})


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {"title": "Contact us", "form": form}
    return render(request, "form.html", context)

