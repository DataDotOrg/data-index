from django.views.generic import TemplateView, CreateView, FormView, DetailView
from . import models, forms
# Create your views here.
class Index(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context

class NewDataset(CreateView):
    model = models.Dataset
    fields = ['name', 'description', 'file']
    template_name = 'main/new_dataset.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Dataset'
        return context

class DataDetails(DetailView):
    model = models.Dataset
    template_name = 'main/data_detail.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Data Details'
        return context

class Search(FormView):
    form_class = forms.SearchForm
    template_name = 'main/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Search'
        return context

class SearchResults(TemplateView):
    template_name = 'main/search_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Search Results'
        return context