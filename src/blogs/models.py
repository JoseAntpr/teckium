from django.db import models
from django.contrib.auth.models import User

DRAFT = 1
PUBLISHED = 2

PUBLICATION_STATUS = ((DRAFT, "Draft"),(PUBLISHED, "Published"))

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250)
    logo = models.ImageField()
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return title


class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField()
    summary = models.CharField(max_length=300)
    content = models.TextField()
    publication_date = models.DateField()
    modified_date = models.DateField(auto_now=True)
    status = models.IntegerField(choices=PUBLICATION_STATUS)

    def __str__(self):
        return title

class Commentary(models.Model):
    content = models.TextField()
    def __str__(self):
        return text
 
class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return name