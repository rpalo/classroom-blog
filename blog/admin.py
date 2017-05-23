from django.contrib import admin
from .models import Blog, Classroom, Post

admin.site.register(Classroom)
admin.site.register(Blog)
admin.site.register(Post)
