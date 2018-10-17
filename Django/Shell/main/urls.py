from django.conf.urls import url, include
urlpatterns = [
    url(r'^/login', include('apps.user_login.urls')),
    url(r'^/dojo', include('apps.dojo_ninja.urls')),
    ]
