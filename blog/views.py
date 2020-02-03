from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .forms import BlogPostModelForm
from .models import BlogPost

# Create your views here.
# def blog_post_detail_page(request, slug):
#     obj = get_object_or_404(BlogPost, slug=slug)
#     template_name = "blog_post_detail.html"
#     context = {"object": obj}
#     return render(request, template_name, context)


# CRUD


def blog_post_list_view(request):
    # List objects
    qs = BlogPost.objects.all()
    template_name = "blog/list.html"
    context = {"object_list": qs}
    return render(request, template_name, context)


def blog_post_create_view(request):
    # create objects
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # obj.title = form.cleaned_data.get("title") + "0"
        obj.save()
        form = BlogPostModelForm()
    template_name = "blog/form.html"
    context = {"form": form}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/detail.html"
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_update_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/update.html"
    context = {"object": obj,"form":""}
    return render(request, template_name, context)


def blog_post_delete_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/delete.html"
    context = {"object": obj}
    return render(request, template_name, context)
