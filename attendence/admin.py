from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.LabStatus)
admin.site.register(models.dailyAttendance)
admin.site.register(models.UserAttendence)