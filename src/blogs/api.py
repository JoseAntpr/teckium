from rest_framework import generics
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter, DjangoFilterBackend
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from blogs.models import Post
from blogs.serializers import PostSerializer, PostListSerializer
from users.models import Profile


class PostListAPIView(generics.ListCreateAPIView):
    #authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'title', 'status')

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == "GET" else PostSerializer

    def get_queryset(self):
        return Post.objects.all()

    def perform_create(self, serializer):
        profile = get_object_or_404(Profile, user=self.request.user)
        serializer.save(owner=profile)


class PostDetailAPIView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
