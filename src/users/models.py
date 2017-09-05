from django.db import models
from django.contrib.auth.models import User

RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = ((RELATIONSHIP_FOLLOWING, 'Following'), (RELATIONSHIP_BLOCKED, 'Blocked'))

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key = True, on_delete=models.CASCADE)
    avatar = models.ImageField()
    bio  = models.CharField(max_length=250, blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True)
    relationships = models.ManyToManyField("self", through= 'Relationship', symmetrical=False, related_name='related_to', blank=True)

    def __str__(self):
        return user.name
  
class Relationship(models.Model):
    from_person = models.ForeignKey(Profile, related_name='from_people')
    to_person = models.ForeignKey(Profile, related_name='to_people')
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)

    def __str__(self):
        return str(self.from_person.user.username) + "sigue a " + str(self.to_person.user.username)

    class Meta: 
        unique_together = (('from_person', 'to_person'),)

    