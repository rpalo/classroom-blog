from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Blog, Post

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'

class ClassroomHomepage(ListView):
    model = Post
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Post.objects.order_by('-date_created')




