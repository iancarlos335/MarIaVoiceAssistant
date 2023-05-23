from django.conf.urls import url
from AudioResponse import views

urlpatterns=[
    url(r'^audioResponse/$', views.iaAudioResponseApi),
    url(r'^audioResponse/([0-9]+)$', views.iaAudioResponseApi)
]