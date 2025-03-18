from django.contrib import admin

from . import models


class DatasetAdmin(admin.ModelAdmin):
    list_display = ['name', 'file', ]


admin.site.register(models.Dataset, DatasetAdmin)
