from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Entry some data into model


class Ariels(models.Model):
    first_name = models.CharField(max_length=50)
    age = models.IntegerField()

    # create string represntation
    def __str__(self):
        return self.first_name
