from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    message = models.CharField(max_length=500)
    uploaded = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

class Comment(models.Model):
    comments = models.CharField(max_length=500)
    uploaded = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

