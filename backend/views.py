from django.shortcuts import render
from rest_framework import viewsets
from .models import Post,Comment
from .serializers import PostSerializer,CommentSerializer
# Create your views here.

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    