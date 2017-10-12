from django.contrib import admin

# Register your models here.
from blogs.models import Post, Tag, Blog, Commentary

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Commentary)