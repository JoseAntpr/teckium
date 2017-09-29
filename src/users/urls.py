from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token

from users.api import UserListAPIView, UserDetailAPIView

urlpatterns = [
    # API User
    url(r'^users/$', UserListAPIView.as_view(), name="users_list_api"),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailAPIView.as_view(), name="users_detail_api"),

    url(r'^auth/', obtain_jwt_token, name="auth"),
]