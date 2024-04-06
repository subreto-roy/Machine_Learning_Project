
from django.urls import path
from .views import DataExtractorAPI

urlpatterns = [
    path('extract/', DataExtractorAPI.as_view(), name='data-extractor'),
]
