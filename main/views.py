from django import http
from django.views.generic import TemplateView, CreateView, FormView, DetailView, ListView

from . import models, forms


class Index(ListView):
    template_name = 'main/index.html'
    model = models.Dataset
    context_object_name = 'datasets'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class NewDataset(CreateView):
    model = models.Dataset
    fields = ['name', 'description', 'file']
    template_name = 'main/new_dataset.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Dataset'
        return context

    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = 'My Dataset'
        initial['description'] = 'This is a dataset'
        return initial

    def form_valid(self, form):
        dataset = form.save()
        print(dataset)
        return http.HttpResponseRedirect(self.success_url)


class DatasetDetail(DetailView):
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
