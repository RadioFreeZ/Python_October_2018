from django.conf.urls import url, include
urlpatterns = [
    url(r'^courses/', include('apps.courses.urls')),
    url(r'^dashboard/', include('apps.login_reg.urls'))
]
