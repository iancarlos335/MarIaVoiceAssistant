from django.urls import path
from . import views

urlpatterns = [
    path('pdf/', views.PdfController.as_view())
]
