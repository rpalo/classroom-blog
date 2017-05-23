from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Blog, Post

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    context_object_name = "blog"

class ClassroomHomepage(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = "all_posts"

    def get_queryset(self):
        return Post.objects.order_by('-date_created')




