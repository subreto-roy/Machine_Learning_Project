# App level urls.py
from django.urls import path
from .views import ExtractionAPIView

urlpatterns = [
    path('extract/', ExtractionAPIView.as_view()),
]

