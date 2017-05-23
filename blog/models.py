from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Post(models.Model):
    
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title