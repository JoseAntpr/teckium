from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter, DjangoFilterBackend
from rest_framework.generics import get_object_or_404


from users.serializers import UserSerializer, UserListSerializer
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

    def perform_create(self, serializer):
        profile = get_object_or_404(Profile, user=self.request.user)
        serializer.save(owner=profile)

'''
class PostDetailAPIView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)



class UsersListSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    username = serializers.CharField()


class UserSerializer(UsersListSerializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        return self.update(User(), validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if validated_data.get('password'):
            instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def validate(self, attrs):
        # si estoy creando un usuario nuevo, comprobar si el username ya está usado
        if self.instance is None and User.objects.filter(username=attrs.get("username")).exists():
            raise ValidationError("Username already exists")

        # actualizo el usuario cambiando el username -> OK si nuevo username no está usado
        if self.instance is not None and self.instance.username != attrs.get("username") and User.objects.filter(
                username=attrs.get("username")).exists():
            raise ValidationError("Username already exists")

        return attrs

'''