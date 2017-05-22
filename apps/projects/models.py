# -*- coding: utf-8 -*-
from django.db import models
import datetime


# Create your models here.
class Project(models.Model):
    """ Project model"""

    title = models.CharField(max_length=200)
    data = models.DateField(default=datetime.date(2000, 1, 1))

    def __str__(self):
        return self.title
