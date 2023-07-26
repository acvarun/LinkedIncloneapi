from django.urls import path,include
from .views import PostViewset,CommentViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', PostViewset , basename='post')
router.register('comment', CommentViewset , basename='comment')

urlpatterns=[
    path('',include(router.urls))
]