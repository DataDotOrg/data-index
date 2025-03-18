from django import forms

from . import models


class CreateDataset(forms.ModelForm):
    class Meta:
        model = models.Dataset