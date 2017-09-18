from django.conf.urls import url, include
from users.api import UserListAPIView

urlpatterns = [
    # API User
    url(r'^users/$', UserListAPIView.as_view(), name="users_list_api"),
]