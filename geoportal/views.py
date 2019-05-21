from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import WorldBorder, Post, Tag


class CitiesListView(ListView):
    template_name = 'cities/city-list.html'
    model = WorldBorder


class CitiesDetailView(DetailView):
    template_name = 'cities/city-detail.html'
    model = WorldBorder


def index(request):
    return render(request, 'index.html', {})


class PostListView(ListView):
    template_name = 'blog.html'
    model = Post


class PostDetailView(DetailView):
    template_name = 'blog-single.html'
    model = Post

    def get(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        return render(request, self.template_name, context={'objects': obj})


class TagListView(ListView):
    template_name = 'blog.html'
    model = Tag

    def get(self, request):
        tag = get_object_or_404(self.model)
        return render(request, self.template_name, context={'tags': tag})
