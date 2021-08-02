from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Newsletter(models.Model):
    email_field = models.EmailField()


class Post(models.Model):
    title = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(blank=True)
    salary = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Job by {self.author} - {self.title}'
