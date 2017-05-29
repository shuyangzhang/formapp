# coding=utf-8
from __future__ import unicode_literals

import datetime
from django.db import models
from django.db.models import CASCADE, SET_NULL, SET_DEFAULT

import random

# Create your models here.

class Wenjuan(models.Model):
    ip = models.CharField(max_length=32, db_index=True)
    post_time = models.DateTimeField(db_index=True)
    name = models.CharField(max_length=32, db_index=True)
    placeRadio = models.CharField(max_length=2, db_index=True)
    placetyped = models.CharField(max_length=32, db_index=True)
    beforeAction = models.CharField(max_length=2, db_index=True)
    jacket = models.CharField(max_length=2, db_index=True)
    trousers = models.CharField(max_length=2, db_index=True)
    temperature = models.CharField(max_length=2, db_index=True)
    confortable = models.CharField(max_length=2, db_index=True)
    totalconf = models.CharField(max_length=2, db_index=True)
    beats = models.CharField(max_length=3, db_index=True)
    lat = models.FloatField(default=0, db_index=True)
    lon = models.FloatField(default=0, db_index=True)
