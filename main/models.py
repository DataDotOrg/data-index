from django.db import models

# Create your models here.
class Dataset(models.Model):
    name = models.CharField(max_length=100)
    data = models.FileField(upload_to='media/')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name