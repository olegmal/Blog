from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView

from rest_framework.viewsets import ModelViewSet

from api.serializers import PostSerializer
from blog.models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(RetrieveAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()

    def get_object(self):
        return Post.objects.filter(post__pk=self.kwargs.get('pk')).first()




