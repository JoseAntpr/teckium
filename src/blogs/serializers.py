from django.contrib.auth.models import User
from rest_framework import serializers

from blogs.models import Post, Tag, Blog


class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        fields = ("id", "title", "description", "logo",
                  "creation_date", "owner", "favourites")
    

class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("id", "title", "status")


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('owner',)


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'
