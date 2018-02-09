# models.py
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=28)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=50, default='default')

    def __unicode__(self):
        return self.name
