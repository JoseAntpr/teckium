from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from blogs.models import Blog
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ('user',)
        read_only_fields = ('creation_date', 'relationships',)


class UserListSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)


class UserSerializer(UserListSerializer):
    password = serializers.CharField(required=False, allow_blank=True)

    profile = ProfileSerializer(required=False)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})

        user = User.objects.create(**validated_data)
        if validated_data.get('password'):
            user.set_password(validated_data.get('password'))
            user.save()
        Profile.objects.create(user=user, **profile_data)
        Blog.objects.create(owner=user, title=user.username)

        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        profile = instance.profile

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if validated_data.get('password'):
            instance.set_password(validated_data.get('password'))

        instance.save()

        profile.user = instance
        print(profile_data)
        profile.avatar = profile_data.get('avatar', profile.avatar)
        profile.bio = profile_data.get('bio', profile.bio)

        profile.save()

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


class UserPostSerializer(UserListSerializer):
    profile = ProfileSerializer()

  

