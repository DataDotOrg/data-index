from django import http
from django.template.defaultfilters import ljust
from django.views.generic import TemplateView, CreateView, FormView, DetailView, ListView
import yaml
from random_words import RandomWords, LoremIpsum
from . import models, forms
from django.conf import settings
rw = RandomWords()
li = LoremIpsum()


class Index(ListView):
    template_name = 'main/index.html'
    model = models.Dataset
    context_object_name = 'datasets'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class NewChoose(TemplateView):
    template_name = 'main/choose_datatype.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Choose Data Type'
        return context

class NewDatasetSchema(CreateView):
    model = models.Dataset
    form_class = forms.CreateDatasetSchema
    template_name = 'main/new_dataset_schema.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Dataset'
        return context

    def get_initial(self):
        initial = super().get_initial()
        if settings.USE_RANDOM_DATA:
            initial['name'] = ' '.join(rw.random_words(count=2))
            initial['description'] = li.get_sentences(2)
            initial['url'] = f"https://{'-'.join(rw.random_words(count=2))}.com"
        return initial


class NewDatasetNoSchema(CreateView):
    model = models.Dataset
    form_class = forms.CreateDatasetNoSchema
    template_name = 'main/new_dataset_no_schema.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Dataset'
        return context

    def get_initial(self):
        initial = super().get_initial()
        if settings.USE_RANDOM_DATA:
            initial['name'] = ' '.join(rw.random_words(count=2))
            initial['description'] = li.get_sentences(2)
            initial['url'] = f"https://{'-'.join(rw.random_words(count=2))}.com"
        return initial


class DatasetDetail(DetailView):
    model = models.Dataset
    template_name = 'main/data_detail.html'
    context_object_name = 'dataset'
    slug_url_kwarg = 'dataset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Data Details'
        with open(self.object.file.path) as file:
            data = yaml.safe_load(file)
        context['file_contents'] = yaml.dump(data, default_flow_style=False)
        return context


