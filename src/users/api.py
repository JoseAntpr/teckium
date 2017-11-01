from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.filters import DjangoFilterBackend


from users.permissions import UserPermission
from users.serializers import UserSerializer, UserListSerializer


# API de User
class UserListAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'username', 'email')
    permission_classes = (UserPermission,)

    def get_serializer_class(self):
        return UserListSerializer if self.request.method == "GET" else UserSerializer

    def get_queryset(self):
        return User.objects.all()


class UserDetailAPIView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)
