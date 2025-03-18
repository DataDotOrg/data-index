from django.db import models

from django.utils.text import slugify


class Dataset(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=110, null=True)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='media/')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
