from django import forms

from . import models


class CreateDatasetSchema(forms.ModelForm):
    class Meta:
        model = models.Dataset
        fields = ['name', 'description', 'file', 'url']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'class': 'form-control'}),
            'file': forms.FileInput(attrs={'accept': '.yaml,.yml,.json', 'class': 'form-control'}),
            'url': forms.URLInput(attrs={'placeholder': 'URL', 'class': 'form-control'}),
        }

class CreateDatasetNoSchema(forms.ModelForm):
    class Meta:
        model = models.Dataset
        fields = ['name', 'description', 'file', 'url']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'class': 'form-control'}),
            'file': forms.FileInput(attrs={'accept': '.csv,.tsv,.txt', 'class': 'form-control'}),
            'url': forms.URLInput(attrs={'placeholder': 'URL', 'class': 'form-control'}),
        }