from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.
def blog_post_detail_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_post_detail.html"
    context = {"object": obj}
    return render(request, template_name, context)


# CRUD


def blog_post_list_view(request):
    # List objects
    qs = BlogPost.objects.all()
    template_name = "blog_post_list.html"
    context = {"object_list": qs}
    return render(request, template_name, context)


def blog_post_retrieve_view(request):
    # create objects
    template_name = "blog_post_create.html"
    context = {"form": ""}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug)
    template_name = "blog_post_detail.html"
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_update_view(request):
    obj = get_object_or_404(BlogPost, slug)
    template_name = "blog_post_update.html"
    context = {"object": obj,"form":""}
    return render(request, template_name, context)


def blog_post_delete_view(request):
    obj = get_object_or_404(BlogPost, slug)
    template_name = "blog_post_delete.html"
    context = {"object": obj}
    return render(request, template_name, context)
