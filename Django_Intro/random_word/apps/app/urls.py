from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^random_word$', views.random),
    url(r'^random_word/reset$', views.reset),
]
