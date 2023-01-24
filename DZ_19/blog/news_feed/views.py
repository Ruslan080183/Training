from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from .models import Page, Post


def say_hello(request):
    return HttpResponse("Hello")


def get_pages_list(request):
    context = {"all_pages": Page.objects.all()}
    return render(request, "all_pages.html", context)


class PostListView(ListView):
    model = Post
    template_name = "all_posts.html"


class PostCreateView(CreateView):
    model = Post
    fields = ["name", "content", "page"]
    template_name = "post_create.html"
    success_url = "/"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ["name", "content"]
    success_url = "/"


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/"
    template_name = "post_delete.html"


class PageCreateView(CreateView):
    model = Page
    fields = ["title", "description", "owner"]
    template_name = "page_create.html"
    success_url = "/"


class PageUpdateView(UpdateView):
    model = Page
    template_name = "page_update.html"
    fields = ["title", "description"]
    success_url = "/"


class PageDeleteView(DeleteView):
    model = Page
    success_url = "/"
    template_name = "page_delete.html"
