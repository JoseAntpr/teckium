# Create your views here.


from users.serializers import UserSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'profile': UserSerializer(user, context={'request': request}).data
    }

