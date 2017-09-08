from django.db import models
from users.models import Profile 

DRAFT = 1
PUBLISHED = 2
PUBLICATION_STATUS = ((DRAFT, "Draft"), (PUBLISHED, "Published"))


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250)
    logo = models.ImageField()
    creation_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    favourites = models.ManyToManyField(
        Profile, related_name="favourites", blank=True)
    mentions = models.ManyToManyField(
        Profile, related_name="mentions", blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField()
    summary = models.CharField(max_length=300)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=PUBLICATION_STATUS)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


class Commentary(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    owner = models.ManyToManyField(Profile)
    answerComment = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.content
 
