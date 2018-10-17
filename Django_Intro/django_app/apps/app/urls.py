from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/$', views.new),
    url(r'^create/$', views.create),
    url(r'^(?P<num>\d{1,4})$', views.show),
    url(r'^(?P<num>\d{1,4})/(edit)$', views.edit),
    url(r'^(?P<num>\d{1,4})/(delete)$', views.delete),
]
