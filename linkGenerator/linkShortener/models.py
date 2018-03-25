from django.core.validators import URLValidator
from django.db import models


# Create your models here.

class LinkModel(models.Model):
    link = models.URLField(validators=[URLValidator()],max_length=200)
    shortLink = models.SlugField(unique=True,max_length=30) #CharField(max_length=30,unique=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.link)
    def __unicode__(self):
        return str(self.link)