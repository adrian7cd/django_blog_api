from ast import Is
from django import views
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser

from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import isAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
  permission_classes = (isAuthorOrReadOnly,)
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAdminUser]
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer


