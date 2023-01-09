from django.db import models

# Create your models here.

class Searchname(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name


from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title
