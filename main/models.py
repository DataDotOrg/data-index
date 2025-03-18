from django.db import models


class Dataset(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='media/')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
