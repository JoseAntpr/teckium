from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter, DjangoFilterBackend
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from blogs.models import Post, Tag, Blog, Commentary
from blogs.serializers import PostSerializer, PostListSerializer, TagSerializer, BlogSerializer, CommentSerializer
from users.models import Profile

# API de Blog


class BlogListAPIView (generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetailAPIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# API de Post


class PostListAPIView(generics.ListCreateAPIView):
    #authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('id', 'title', 'status', 'tags', 'owner')
    ordering_fields = ('-publication_date',)
    ordering = ('-publication_date',)

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == "GET" else PostSerializer

    def get_queryset(self):
        return Post.objects.all()

    def perform_create(self, serializer):
        profile = get_object_or_404(Profile, user=self.request.user)
        serializer.save(owner=profile)


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)


# API de Tag


class TagListAPIView(generics.ListCreateAPIView):
    #authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'name',)


class TagDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    #authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'name',)


class CommentListAPIView(generics.ListCreateAPIView):
    queryset = Commentary.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ('-publication_date',)
    ordering = ('-publication_date',)
    filter_fields = ('post',)
    