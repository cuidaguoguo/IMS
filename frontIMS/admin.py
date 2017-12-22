# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# register your models here.
import models

admin.site.register(models.Student)
admin.site.register(models.Institude)
admin.site.register(models.Teacher)
admin.site.register(models.Couser)
admin.site.register(models.Major)
admin.site.register(models.Grade)
admin.site.register(models.Score)

