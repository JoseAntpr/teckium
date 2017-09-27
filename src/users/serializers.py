from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ('user',)


class UserListSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class UserSerializer(UserListSerializer):
    password = serializers.CharField()

    profile = ProfileSerializer()

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)

        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if validated_data.get('password'):
            instance.set_password(validated_data.get('password'))

        instance.save()

        profile.user = instance
        profile.avatar = profile_data.get('avatar', profile.avatar)
        profile.bio = profile_data.get('bio', profile.bio)

        profile.save()

        return instance


class UserPostSerializer(UserListSerializer):
    profile = ProfileSerializer()

  

