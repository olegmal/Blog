from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import PostSerializer
from blog.models import Post
from core.permissions import IsSuperuser

# class PostViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsSuperuser]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostListView(ListAPIView):
    # permission_classes = [IsSuperuser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(RetrieveAPIView):
    # permission_classes = [IsSuperuser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
