from django.conf.urls import url, include
from .views import index, home


urlpatterns = [
    url(r'^$', index, name="index"),
]
