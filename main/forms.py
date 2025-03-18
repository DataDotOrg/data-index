from django import forms

from . import models


class CreateDataset(forms.ModelForm):
    class Meta:
        model = models.Dataset
        fields = ['name', 'file', ]


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)