from django.db import models
from django.contrib.auth.models import User

class Classroom(models.Model):

    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):

    user = models.ForeignKey(User, related_name="blogs", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, related_name="blogs", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Post(models.Model):
    
    blog = models.ForeignKey(Blog, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    body = models.TextField()

    def author(self):
        user = self.blog.user
        return user.first_name

    def __str__(self):
        return self.title

