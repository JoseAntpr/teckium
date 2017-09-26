from django.conf.urls import url, include
from blogs.api import PostListAPIView, PostDetailAPIView, TagListAPIView, TagDetailAPIView, BlogListAPIView, BlogDetailAPIView

urlpatterns = [
    # API POST
    url(r'^posts/$', PostListAPIView.as_view(), name="posts_list_api"),
    url(r'^posts/(?P<pk>[0-9]+)/$', PostDetailAPIView.as_view(), name="posts_detail_api"),

    # API TAG
    url(r'^tags/$', TagListAPIView.as_view(), name="tags_list_api"),
    url(r'^tags/(?P<pk>[0-9]+)/$', TagDetailAPIView.as_view(), name="posts_detail_api"),

    # API BLOG
    url(r'^blogs/$', BlogListAPIView.as_view(), name="blogs_list_api"),
    url(r'^blogs/(?P<pk>[0-9]+)/$', BlogDetailAPIView.as_view(), name="blogs_detail_api"),
]
