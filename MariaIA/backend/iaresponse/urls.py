from django.urls import path
from . import views

urlpatterns = [
    path('audio/', views.IaVoiceResponse.as_view())
]


