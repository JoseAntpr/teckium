from django.db import models
from django.contrib.auth.models import User

DRAFT = 1
PUBLISHED = 2
PUBLICATION_STATUS = ((DRAFT, "Draft"), (PUBLISHED, "Published"))


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    favourites = models.ManyToManyField(
        User, related_name="favourites", blank=True)
    mentions = models.ManyToManyField(
        User, related_name="mentions", blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(blank=True, null=True)
    summary = models.CharField(max_length=300, blank=True, null=True)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=PUBLICATION_STATUS)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


class Commentary(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    owner = models.ManyToManyField(User)
    answerComment = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.content

