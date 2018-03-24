from django.db import models


# Create your models here.

class LinkModel(models.Model):
    link = models.CharField(max_length=500)
    shortLink = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return str(self.link)
    def __unicode__(self):
        return str(self.link)