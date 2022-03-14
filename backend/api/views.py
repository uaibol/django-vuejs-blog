from django.shortcuts import render
from post.models import Post, Comment
from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import F


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.increase_view_count()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
      

class CommentList(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
