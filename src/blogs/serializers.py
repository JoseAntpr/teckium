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
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'image', 'summary', 'content', 'publication_date',
                  'status', 'blog', 'owner', 'tags', 'comments', 'likes')
        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):
    owner = UserPostSerializer()

    class Meta:
        model = Commentary
        fields = '__all__'
    
    def create(self, validated_data):
        owner_data = validated_data.pop('owner')

        comment = Commentary.objects.create(**validated_data)
        user = User.objects.get(username=owner_data.get('username'))
        comment.owner = user
        comment.save()

        return comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commentary
        fields = '__all__'


        

