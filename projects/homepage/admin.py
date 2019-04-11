from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Weight)
admin.site.register(models.patients)