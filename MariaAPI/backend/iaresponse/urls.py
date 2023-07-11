from django.urls import path
from . import views

urlpatterns = [
    path('audio/<int:id>', views.GetIaResponseData.post, name='audio')
]