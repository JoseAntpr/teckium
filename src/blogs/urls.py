from django.conf.urls import url, include
from blogs.api import PostListAPIView, PostDetailAPIView

urlpatterns = [
    # API POST
    url(r'^posts/$', PostListAPIView.as_view(), name="posts_list_api"),
    url(r'^posts/(?P<pk>[0-9]+)/$', PostDetailAPIView.as_view(), name="posts_detail_api"),
]
