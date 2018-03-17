# -*- coding: utf-8 -*-

from django.db import models


class EventManager(models.Manager):
    def create_event(self, **kwargs):
        return self.create(kwargs)

    
class Event(models.Model):
    artist = models.CharField(max_length= 100)
    location = models.CharField(max_length= 100)
    date = models.CharField(max_length= 100)

    objects = EventManager()
