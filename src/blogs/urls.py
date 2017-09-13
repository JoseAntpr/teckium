from django.conf.urls import url, include
from blogs.api import PostListAPIView

urlpatterns = [
    # API POST
    url(r'^posts/$', PostListAPIView.as_view(), name="posts_list_api"),
    # DOC del API
    url(r'^docs', include('rest_framework_docs.urls')),
]
