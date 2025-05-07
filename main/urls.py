from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    # list
    path('', views.Index.as_view(), name='index'),
    # create dataset
    path('new/', views.NewChoose.as_view(), name='new_choose'),
    path('new/schema/', views.NewDatasetSchema.as_view(), name='create_dataset_schema'),
    path('new/no-schema/', views.NewDatasetNoSchema.as_view(), name='create_dataset_no_schema'),
    # details
    path('dataset/<str:dataset>/', views.DatasetDetail.as_view(), name='dataset_detail'),
]
