from rest_framework import serializers
from post.models import Post, Category, Comment

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id','author', 'title', 'image', 'excerpt', 'content', 'category', 'slug', 'view_count')

       
class PostDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ('id','author', 'title', 'image', 'content', 'category', 'slug', 'view_count', 'comments')
    
    def get_comments(self, obj):
        queryset = Comment.objects.filter(post=obj)
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('post', 'name', 'content', 'created_date')

        

