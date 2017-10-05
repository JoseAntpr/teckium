import rest_framework_jwt
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter, DjangoFilterBackend
from rest_framework.generics import get_object_or_404


from users.serializers import UserSerializer, UserListSerializer, ProfileSerializer
from users.models import Profile


# API de User
class UserListAPIView(generics.ListCreateAPIView):
    #authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'username', 'email')

    def get_serializer_class(self):
        return UserListSerializer if self.request.method == "GET" else UserSerializer

    def get_queryset(self):
        return User.objects.all()


class UserDetailAPIView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
