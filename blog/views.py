from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'
