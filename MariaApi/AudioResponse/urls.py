from django.urls import re_path
from AudioResponse import views

urlpatterns=[
    re_path(r'^audioResponse/$', views.iaAudioResponseApi),
    re_path(r'^audioResponse/([0-9]+)$', views.iaAudioResponseApi)
]