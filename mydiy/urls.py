from django.urls import path
from django.conf.urls import include, url
from mydiy.views import user

urlpatterns = [
    url(r'users/', user)
]