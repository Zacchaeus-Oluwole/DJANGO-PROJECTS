from django.db import models

# Create your models here.

class Post(models.Model):
    slackUsername = models.CharField(max_length=100)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.slackUsername