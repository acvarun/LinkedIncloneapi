from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Post(models.Model):
    message = models.CharField(max_length=500)
    uploaded = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='post')

    def __str__(self):
        return self.message

class Comment(models.Model):
    comments = models.CharField(max_length=500)
    uploaded = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')


