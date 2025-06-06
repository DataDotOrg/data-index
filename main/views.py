from django import http
from django.template.defaultfilters import ljust
from django.views.generic import TemplateView, CreateView, FormView, DetailView, ListView
import yaml
from random_words import RandomWords, LoremIpsum
from . import models, forms
from django.conf import settings
import subprocess
import os
import pandas as pd

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

    def form_valid(self, form):
        # Save the dataset instance
        dataset = form.save()

        # Path to the uploaded file
        file_path = dataset.file.path  # Assuming `file` is the field for the uploaded file

        # Generate schema using Frictionless
        schema_path = os.path.splitext(file_path)[0] + ".schema.yaml"
        try:
            subprocess.run(
                ["frictionless", "describe", "--yaml", "--type", "schema", file_path],
                check=True,
                stdout=open(schema_path, "w")  # Save the schema to a file
            )
        except subprocess.CalledProcessError as e:
            # Handle errors in schema generation
            print(f"Error generating schema: {e}")
            # Optionally, add error handling logic here

        return super().form_valid(form)


class DatasetDetail(DetailView):
    model = models.Dataset
    template_name = 'main/data_detail.html'
    context_object_name = 'dataset'
    slug_url_kwarg = 'dataset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Data Details'
        file_path = self.object.file.path  # Path to the uploaded file
        schema_path = os.path.splitext(file_path)[0] + ".schema.yaml"  # Path to the generated schema file

        try:
            # Check if the schema file exists
            if os.path.exists(schema_path):
                # Parse the Frictionless schema file
                with open(schema_path) as schema_file:
                    schema_data = yaml.safe_load(schema_file)
                context['file_contents'] = yaml.dump(schema_data, default_flow_style=False)  # YAML-formatted schema
            else:
                # Fallback to displaying the file contents
                if file_path.endswith('.yaml') or file_path.endswith('.yml'):
                    # Parse YAML file
                    with open(file_path) as file:
                        data = yaml.safe_load(file)
                    context['file_contents'] = yaml.dump(data, default_flow_style=False)
                elif file_path.endswith('.csv'):
                    # Parse CSV file
                    data = pd.read_csv(file_path)  # Read CSV file into a DataFrame
                    csv_as_dict = data.to_dict(orient='records')  # Convert DataFrame to a list of dictionaries
                    context['file_contents'] = yaml.dump(csv_as_dict, default_flow_style=False)
                else:
                    context['file_contents'] = "Unsupported file format."
        except Exception as e:
            context['file_contents'] = f"Error reading file: {e}"

        return context


