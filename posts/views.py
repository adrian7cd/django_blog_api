from rest_framework import generics

from .models import Post
from .serializers import PostSerializer
from .permissions import isAuthorOrReadOnly

class PostList(generics.ListCreateAPIView):
  permission_classes = (isAuthorOrReadOnly,)
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (isAuthorOrReadOnly,)
  queryset = Post.objects.all()
  serializer_class = PostSerializer

  