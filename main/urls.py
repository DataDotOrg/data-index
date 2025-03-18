from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    # list
    path('', views.Index.as_view(), name='index'),
    # create dataset
    path('new/', views.NewDataset.as_view(), name='create_dataset'),
    # details
    path('dataset/<str:dataset>/', views.DatasetDetail.as_view(), name='dataset_detail'),
    # search
    path('search/', views.Search.as_view(), name='search'),
    path('search-results/', views.SearchResults.as_view(), name='search_results'),
]
