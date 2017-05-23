from django.db import models
from django.contrib.auth.models import User

class Classroom(models.Model):

    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/classrooms/{}".format(self.pk)

class UserProfile(models.Model):

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    classrooms = models.ManyToManyField(Classroom)

    def __str__(self):
        return "{} Profile".format(self.user.username)

    def is_enrolled(self):
        return self.classroom is not None

class Blog(models.Model):

    user = models.ForeignKey(User, related_name="blogs", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, related_name="blogs", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blogs/{}".format(self.pk)

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

    def get_absolute_url(self):
        return "/posts/{}".format(self.pk)

