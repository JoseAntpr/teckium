"""teckium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

import blogs
#from blogs.api import PostViewSet

#router = DefaultRouter()
#router.register("posts", PostViewSet, base_name="posts_api")

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # API
    url(r'^api/1.0/', include('blogs.urls')),
    url(r'^api/1.0/', include('users.urls')),
    #url(r'^api/1.0/', include(router.urls)),

    # DOC del API
    url(r'^$', include('rest_framework_docs.urls')),

]
