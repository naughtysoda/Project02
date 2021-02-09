from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    firstname = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    star = models.IntegerField(default=0,null=True)

    def __str__(self):
        return "{}-{}".format(self.firstname,self.star)

