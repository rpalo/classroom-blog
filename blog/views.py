from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Blog, Classroom, Post

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    context_object_name = "blog"

class ClassroomHomepage(LoginRequiredMixin, DetailView):
    model = Classroom
    template_name = 'classroom/index.html'
    context_object_name = "classroom"

    def get_context_data(self, **kwargs):
        context = super(ClassroomHomepage, self).get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(blog__classroom=self.object).order_by("-date_created")
        return context




