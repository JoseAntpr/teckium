from django.contrib.auth.models import User
from rest_framework import serializers

from blogs.models import Post, Tag, Blog, Commentary
from users.serializers import UserPostSerializer


class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        fields = ("id", "title", "description", "logo",
                  "creation_date", "owner", "favourites")
    

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    owner = UserPostSerializer()
    blog = BlogSerializer()

    class Meta:
        model = Post
        fields = "__all__"
        

class PostSerializer(serializers.ModelSerializer):
    owner = UserPostSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('owner',)


class CommentSerializer(serializers.ModelSerializer):
    owner = UserPostSerializer()
    
    class Meta:
        model = Commentary
        fields = '__all__'
        

