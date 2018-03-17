# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from api.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'artist',
        'location',
        'date'
    )

admin.site.register(Event, EventAdmin)