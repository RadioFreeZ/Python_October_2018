from django.conf.urls import url, include
urlpatterns = [
    url(r'^courses/', include('apps.courses.urls'))
]
